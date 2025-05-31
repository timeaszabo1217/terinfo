from qgis.PyQt.QtCore import QVariant
from qgis.core import *

telepulesek = QgsProject.instance().mapLayersByName('Települések fehér')[0]
pontok = QgsProject.instance().mapLayersByName('Éttermek, bárok és kávézók')[0]

telepulesek.startEditing()

fields = [field.name() for field in telepulesek.fields()]
if 'etterem_db' not in fields:
    telepulesek.dataProvider().addAttributes([QgsField('etterem_db', QVariant.Int)])
if 'bar_db' not in fields:
    telepulesek.dataProvider().addAttributes([QgsField('bar_db', QVariant.Int)])
if 'kavezo_db' not in fields:
    telepulesek.dataProvider().addAttributes([QgsField('kavezo_db', QVariant.Int)])

telepulesek.updateFields()

for telepules in telepulesek.getFeatures():
    geom = telepules.geometry()
    etterem_count = 0
    bar_count = 0
    kavezo_count = 0

    for pont in pontok.getFeatures():
        if geom.contains(pont.geometry()):
            if pont['amenity'] == 'restaurant':
                etterem_count += 1
            elif pont['amenity'] == 'bar':
                bar_count += 1
            elif pont['amenity'] == 'cafe':
                kavezo_count += 1

    telepules['etterem_db'] = etterem_count
    telepules['bar_db'] = bar_count
    telepules['kavezo_db'] = kavezo_count
    telepulesek.updateFeature(telepules)

telepulesek.commitChanges()

symbol_rest = QgsMarkerSymbol.createSimple({'name': 'circle', 'color': '#008837'})
symbol_bar = QgsMarkerSymbol.createSimple({'name': 'triangle', 'color': '#7b3294'})
symbol_cafe = QgsMarkerSymbol.createSimple({'name': 'square', 'color': '#efebf1'})

rules = [
    ('Étterem', '"amenity" = \'restaurant\'', symbol_rest),
    ('Bár', '"amenity" = \'bar\'', symbol_bar),
    ('Kávézó', '"amenity" = \'cafe\'', symbol_cafe)
]

root_rule = QgsRuleBasedRenderer.Rule(None)
for label, expression, symbol in rules:
    rule = QgsRuleBasedRenderer.Rule(symbol)
    rule.setLabel(label)
    rule.setFilterExpression(expression)
    root_rule.appendChild(rule)

renderer = QgsRuleBasedRenderer(root_rule)
pontok.setRenderer(renderer)
pontok.triggerRepaint()