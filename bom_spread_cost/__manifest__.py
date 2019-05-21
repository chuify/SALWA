{
    'name': 'BOM spread cost',
    'description': """
1. The BOM cost is fully assigned to the primary product only instead of assigning some of the cost to the byproduct. Its like the byproduct is free with no cost of production as the full production cost goes to the primary product. How can the cost be assigned proportionately to the main product and the byproduct depending on the % of components or portion of material used? For example : 

Manufacture product : 0.95 Qty 
Compo  1: Cost = 100
Compo  2: Cost = 200
Byproduct : 0.05 Qty
Manufacture product + byproduct = 1 unit
Costs of all compo = 100 + 200 = 300 

Here the cost has to be split regarding the proportion of units used for the main product and for the byproduct.
95% of 300 ==> 285 
5% of 300 ==>  15

2. This information above( with the split of the cost) also has to appear on the BoM Structure & Cost report. Now we only have the full cost assigned to the main product + we don't see the byproduct on the report. 

3. Following above, we will get the cost on the byproduct through the BOM. This cost will also have to appear automatically in the product form of the byproduct. Through maybe an action saying ' Update the cost', if this product is a byproduct. 

4. Adding a new column on the report BoM Structure & Cost with the unit cost of all the products : Main product + components + Byproduct. ( see picture 1)
    """,
    'version': '12.0.0',
    'depends': ['base', 'product', 'mrp', 'mrp_byproduct', 'mrp_bom_cost'],
    'data': [
        'views.xml',
        'reports.xml',
    ],
}
