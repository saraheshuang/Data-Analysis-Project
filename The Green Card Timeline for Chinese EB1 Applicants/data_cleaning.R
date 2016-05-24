#The original data of eb1 Chinese applicants were saved in two google spreadsheet based on online voluntray contribution.
#This R files cleaned and transformed these two datasets and merged them into one dataset called eb1data.csv 

#import dataset
##setwd("/Users/heshuangzeng/Documents/my_data_vis_projet/eb1/")
nsc<-read.csv("EB1 485 Timeline Update to 072415 - NSC.csv")
tsc<-read.csv("EB1 485 Timeline Update to 072415 - TSC.csv")
str(nsc)
str(tsc)
nsc$center<-"NSC"
tsc$center<-"TSC"

#convert important variables: 
#as.Date to covert 485RD_Date(Date), FP_Date(Date) to Date data

nsc$X485RD_Date<-as.Date (nsc$X485.RD, "%m/%d/%Y")
nsc$FP_Date<-as.Date (nsc$FP.Date, "%m/%d/%Y")
nsc$AP_EAD_Date<-as.Date(nsc$AP...EAD..Approved..Date,"%m/%d/%Y")
nsc$X485AD_Date<-as.Date(nsc$X485.AD,"%m/%d/%Y")
tsc$X485RD_Date<-as.Date(tsc$I.485.Received..Date,"%m/%d/%Y")
tsc$FP_Date<-as.Date (tsc$FP.Date, "%m/%d/%Y")
tsc$AP_EAD_Date<-as.Date(tsc$AP...EAD..Approved..Date,"%m/%d/%Y")
tsc$X485AD_Date<-as.Date(tsc$X485..Approved..Date,"%m/%d/%Y")

#extract state information
#1-covert factor to character
nsc$state<-as.character(nsc$X.1)
tsc$state<-as.character(tsc$Walk.in.Office.Location)
#2-use stringr extract function, extract string that meets the requirement
library(stringr)
state_nsc<-str_extract(nsc$state, "[A-Z][A-Z]")
state_tsc<-str_extract(tsc$state, "[A-Z][A-Z]")
nsc$State<-state_nsc
tsc$State<-state_tsc

#extract the fileds that matter for each dataset
nsc_new<-data.frame(nsc$X485RD_Date,nsc$FP_Date,nsc$AP_EAD_Date, nsc$X485AD_Date, nsc$Center, nsc$Type, nsc$State)
tsc_new<-data.frame(tsc$X485RD_Date,tsc$FP_Date,tsc$AP_EAD_Date, tsc$X485AD_Date, tsc$Center, tsc$Type, tsc$State)
names(nsc_new)<-c("X485RD_Date", "FP_Date", "AP_EAD_Date", "X485AD_Date", "Center", "Type", "State")
names(tsc_new)<-c("X485RD_Date", "FP_Date", "AP_EAD_Date", "X485AD_Date", "Center", "Type", "State")
eb1data<-rbind(nsc_new, tsc_new)

#extract data type
Type<-str_extract(eb1data$Type, "[eE][Bb]1[aAbBcC]")
eb1data$Type<-as.factor(tolower(Type))

#as.numeric(as.character()) to covert factors to numeric for Days_RDtoFP_Notice_Date(number), Days_RDto.EAD.AP.AD(number), Days_FPto485AD(number),Days_RDtoGC(number)
eb1data$Days_RDtoFP<-as.numeric(eb1data$FP_Date-eb1data$X485RD_Date)
eb1data$Days_FPtoEAD<-as.numeric(eb1data$AP_EAD_Date-eb1data$FP_Date)
eb1data$Days_EADto485AD<-as.numeric(eb1data$X485AD_Date-eb1data$AP_EAD_Date)
eb1data$Days_RDto485AD<-as.numeric(eb1data$X485AD_Date-eb1data$X485RD_Date)

#exclude the outliers
eb1data<-subset(eb1data,eb1data$Days_RDto485AD<365)

#further clean the States' data, remove the invalid value
states<-c("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")
lapply(eb1data$State, function(x) if (x %in% states) {x} else {NA})


#extract Year&Month information
eb1data$Year<-as.numeric(format(eb1data$X485RD_Date,"%Y"))
eb1data$Month<-as.numeric(format(eb1data$X485RD_Date,"%M"))

#export data to csv
write.csv(eb1data, "eb1data.csv")
