from django.contrib import admin
from .models import State,City,Area,User,Order,Product,order_details,Order_return,Company,Inquery,Cart
from .models import Compliant,Brand,Offer,Feature,Category,Sub_category,Order_return_details,connectus,Cartfinal,Feedback,Complaints
# Register your models here.
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def export_to_pdf(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['U_id', 'tamount', 'payment','datetime']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.user_id,obj.Pay_amount,obj.Payment_date])



   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to PDF"
def export_to_pdf2(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['Product_name','price','quantity','subcategory']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.product_name,obj.price,obj.quantity_on_hand,obj.sub_category_id ])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to Product"


def export_to_pdf3(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ['feedback','date','product_id','user_id']

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.feedback,obj.date,obj.product_id,obj.user_id ])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to Feedback"


def export_to_orderdetails(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers = ["order_id","product_id","price","quantity","user_id"]

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.order_id,obj.product_id,obj.price,obj.quantity,obj.user_id ])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to order_details"

def export_to_pdf4(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers =["id","First_name","Last_name","Email_id","Contact_number","Address","Security_Que","Security_Answer"]

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.id,obj.First_name,obj.Last_name,obj.Email_id,obj.Contact_number,obj.Address,obj.Security_Que,obj.Security_Answer])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description ="Export to user"
def export_to_pdf5(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers =["compliant_details","user_id"]

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.compliant_details,obj.user_id])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to Complaint"

def export_to_pdf5(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers =["id","sub_category_name","category_id"]

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.id,obj.sub_category_name,obj.category_id])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to subcategory"

def export_to_pdf6(modeladmin, request, queryset):
   # Create a new PDF
   response = HttpResponse(content_type='application/pdf')
   response['Content-Disposition'] = 'attachment; filename="report.pdf"'

   # Generate the report using ReportLab
   doc = SimpleDocTemplate(response, pagesize=letter)

   elements = []

   # Define the style for the table
   style = TableStyle([
       ('BACKGROUND', (0,0), (-1,0), colors.grey),
       ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
       ('ALIGN', (0,0), (-1,-1), 'CENTER'),
       ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
       ('FONTSIZE', (0,0), (-1,0), 14),
       ('BOTTOMPADDING', (0,0), (-1,0), 12),
       ('BACKGROUND', (0,1), (-1,-1), colors.beige),
       ('GRID', (0,0), (-1,-1), 1, colors.black),
   ])

   # Create the table headers
   headers =["id","category_name"]

   # Create the table data
   data = []
   for obj in queryset:
       data.append([obj.id,obj.category_name])

   # Create the table
   t = Table([headers] + data, style=style)

   # Add the table to the elements array
   elements.append(t)

   # Build the PDF document
   doc.build(elements)

   return response

export_to_pdf.short_description = "Export to category"






class Show_company(admin.ModelAdmin):
    list_display = ["company_name","contact","email","address"]
    list_filter = ["company_name","contact","email","address"]
    search_fields = ["company_name","contact","email","address"]

class Show_State(admin.ModelAdmin):
    list_display = ["state_name"]
    list_filter =  ["state_name"]
    search_fields = ["state_name"]


class Show_City(admin.ModelAdmin):
    list_display = ["city_name","state"]
    list_filter = ["city_name","state"]
    search_fields = ["city_name","state"]

class Show_Area(admin.ModelAdmin):
    list_display = ["area_name","city"]
    list_filter = ["area_name","city"]
    search_fields = ["area_name","city"]

class Show_User(admin.ModelAdmin):
    list_display = ["id","First_name","Last_name","Email_id","Contact_number","Password","Address","Security_Que","Security_Answer","area","user_photo"]
    list_filter = ["id","First_name","Last_name","Email_id","Contact_number","Password","Address","Security_Que","Security_Answer","area","image2"]
    search_fields = ["id","First_name","Last_name","Email_id","Contact_number","Password","Address","Security_Que","Security_Answer","area","user_photo"]
    actions=[export_to_pdf4]

class Show_order(admin.ModelAdmin):
    list_display = ["id","Pay_amount","Payment_date","Payment_status","cgst","sgst","user_id","is_order_cancel","address"]
    list_filter =  ["id","Pay_amount","Payment_date","Payment_status","cgst","sgst","user_id","is_order_cancel","address"]
    search_fields = ["id","Pay_amount","Payment_date","Payment_status","cgst","sgst","user_id","is_order_cancel","address"]
    actions = [export_to_pdf]


class Show_product(admin.ModelAdmin):
    list_display = ['id',"product_name","product_description","price","quantity_on_hand",'sub_category_id','image_path']
    list_filter = ['id',"product_name","product_description","price","quantity_on_hand",'sub_category_id','image_path']
    search_fields = ['id',"product_name","product_description","price","quantity_on_hand",'sub_category_id','image_path']
    actions = [export_to_pdf2]

class Show_order_details(admin.ModelAdmin):
    list_display = ["order_id","product_id","price","quantity","user_id"]
    list_filter =  ["product_id","order_id","price","quantity","user_id"]
    search_fields =  ["product_id","order_id","price","quantity","user_id"]
    actions=[export_to_orderdetails]


class Show_order_return(admin.ModelAdmin):
    list_display = ["order_id","order_return_date","order_return_amt"]
    list_filter = ["order_id","order_return_date","order_return_amt"]
    search_fields = ["order_id","order_return_date","order_return_amt"]

class Show_order_return_details(admin.ModelAdmin):
    list_display = ["return_reason","return_qoh"]
    list_filter = ["return_reason","return_qoh"]
    search_fields = ["return_reason","return_qoh"]

class Show_inquery(admin.ModelAdmin):
    list_display = ["id","inquery_description","inquery_date","user_id","response"]
    list_filter = ["inquery_description","inquery_date","user_id","response"]
    search_fields = ["inquery_description","inquery_date","user_id","response"]

class Show_cart(admin.ModelAdmin):
    list_display = ["quantity","product_id","user_id","product_status","orderid","totalprice"]
    list_filter = ["quantity","product_id","user_id","product_status","orderid","totalprice"]
    search_fields = ["quantity","product_id","user_id","product_status","orderid","totalprice"]

class Show_cartfinal(admin.ModelAdmin):
    list_display = ["quantity","product_id","product_status"]
    list_filter = ["quantity","product_id","product_status"]
    search_fields = ["quantity","product_id","product_status"]

class Show_compliant(admin.ModelAdmin):
    list_display = ["compliant_description","compliant_date","product_id","user_id"]
    list_filter = ["compliant_description","compliant_date","product_id","user_id"]
    search_fields = ["compliant_description","compliant_date","product_id","user_id"]

class Show_Complaints(admin.ModelAdmin):
    list_display = ["compliant_details","user_id"]
    list_filter = ["compliant_details","user_id"]
    search_fields = ["compliant_details","user_id"]
    actions = [export_to_pdf5]

class Show_brand(admin.ModelAdmin):
    list_display = ["brand_name"]
    list_filter = ["brand_name"]
    search_fields = ["brand_name"]

class Show_connectus(admin.ModelAdmin):
    list_display = ["name","email","subject_here","details"]
    list_filter = ["name","email","subject_here","details"]
    search_fields = ["name","email","subject_here","details"]

class Show_offer(admin.ModelAdmin):
    list_display = ["id","offer_description","Start_date","End_date","discount","product_id"]
    list_filter = ["offer_description","Start_date","End_date","discount","product_id"]
    search_fields = ["offer_description","Start_date","End_date","discount","product_id"]

class Show_feature(admin.ModelAdmin):
    list_display = ["feature_name","feature_description"]
    list_filter = ["feature_name","feature_description"]
    search_fields = ["feature_name","feature_description"]

class Show_category(admin.ModelAdmin):
    list_display = ["id","category_name"]
    list_filter = ["id","category_name"]
    search_fields = ["id","category_name"]
    actions = [export_to_pdf6]


class Show_Sub_category(admin.ModelAdmin):
    list_display = ["id","sub_category_name","category_id"]
    list_filter = ["id","sub_category_name","category_id"]
    search_fields = ["id","sub_category_name","category_id"]
    actions = [export_to_pdf5]

class Show_feedback(admin.ModelAdmin):
    list_display = ["id","feedback","date","product_id","user_id"]
    list_filter = ["id","feedback","date","product_id","user_id"]
    search_fields = ["id","feedback","date","product_id","user_id"]
    actions=[export_to_pdf3]

admin.site.register(Feedback,Show_feedback)

admin.site.register(Order,Show_order)
admin.site.register(order_details,Show_order_details)
admin.site.register(Company,Show_company)
admin.site.register(Complaints,Show_Complaints)
admin.site.register(Inquery,Show_inquery)
admin.site.register(Cart,Show_cart)
admin.site.register(Offer,Show_offer)
admin.site.register(Category,Show_category)
admin.site.register(Sub_category,Show_Sub_category)
admin.site.register(User,Show_User)
admin.site.register(Product,Show_product)
admin.site.register(connectus,Show_connectus)

