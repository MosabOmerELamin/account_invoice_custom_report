{
    "name": "Account Invoice Custom Report",
    "version": "18.0.1.0.0",
    "summary": "Custom invoice PDF layout with bilingual and RTL support",
    "description": "Custom invoice template: rounded header, two info boxes, content area and footer. Supports Arabic/English.",
    "author": "Your Name",
    "category": "Accounting",
    "license": "LGPL-3",
    "depends": ["account", "web"],
    "data": [
        "views/action_report_invoice_bilingual.xml",
        "views/report_invoice_inherit.xml",
        "views/res_company_view.xml"
    ],

    "installable": True,
    "application": True,
}
