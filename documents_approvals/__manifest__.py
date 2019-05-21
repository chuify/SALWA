{
    'name': 'Documents Approvals',

    'description': """
5.0 Ensure Sales Order can be approved by either the finance manager or the Sales manager or BOTH before SO is confirmed in the system 
- Add Sales Manager Approval- Add Finance manager ApprovalWhat we could do is create 2 booleans fields on the SO form. Only visible for the people who have the access rights : Finance Manager + Sales Manager.One field = Finance Manager + one field = Sales Manager. When one of those fields are filled then the button "confirm" appear. If the SO has to be approved by both of them, they will just write a note by notifying the other ==> Standard 5.1 Show signatures of approvers electronically on the Sales order if printed.When a boolean (or both) is (are) checked then on the Sale order the signature of the people ( FM or SM) have to appear.  5.2 Disable Printing of sales Order by the sales agent until approved by the managers. Only after the SO is approved by sales manager or Finance manager pr both, then enable the print option.

==> The person who don't have the access rights Sales Manager + Finance Manager can only print the SO when the SO is confirmed.

5.3 Do the same : 5.0, 5.1 & 5.2 for the model : Purchase Order.

AR : Sales Manager ==> Purchase Manager

6. Restrict invoice creation to only finance (Accountant, Billing role and Advisor)

7. Retrict Chart of accounts and Journals creation to only the Accountant 
    """,

    'version': '12.0.1',

    'depends': ['account', 'sale', 'purchase', 'account_accountant'],

    'data': [
        'views.xml',
        'reports.xml',
        'ir.model.access.csv',
    ],

    'demo': [
    ]
}
