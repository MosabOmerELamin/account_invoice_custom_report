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
        "views/report_invoice_inherit.xml",
    ],
    "assets": {
        "web.assets_common": [
            "account_invoice_custom_report/static/src/scss/invoice_custom.scss",
        ],
        "web.assets_qweb": [],
    },
    "installable": True,
    "application": True,
}