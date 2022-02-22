from django.http import HttpResponse , HttpResponseNotFound
from django.shortcuts import render


def monthlychallanges(request, month):
    challange_text = None
    if month == "january":
        challange_text = "This is the january page"
    elif month == "february":
        challange_text = "This is the february page"
    elif month == "march":
        challange_text = "This is the march page"    
    elif month == "april":
        challange_text = "This is the april page"  
    elif month == "may":
        challange_text = "This is the may page"  
    elif month == "june":
        challange_text = "This is the june page"   
    elif month == "july":
        challange_text = "This is the july page"        
    elif month == "august":
        challange_text = "This is the august page"     
    elif month == "september":
        challange_text = "This is the september page" 
    elif month == "october":
        challange_text = "This is the october page"   
    elif month == "november":
        challange_text = "This is the november page" 
    elif month == "december":
        challange_text = "This is the december page"  
    else:
        return HttpResponseNotFound("path does not exit")      
    return HttpResponse(challange_text)