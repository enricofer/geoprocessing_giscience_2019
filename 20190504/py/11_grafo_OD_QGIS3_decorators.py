from qgis.processing import alg

from PyQt5.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsFields,QgsField,QgsFeature,QgsGeometry, QgsWkbTypes, QgsRaster)

@alg(name="origine_destinazione", label="Crea grafo origine/destinazione", group="customscripts", group_label=alg.tr("Custom Scripts"))
@alg.input(type=alg.SOURCE, name='INPUT_LINEE', label="linee", types=[QgsProcessing.TypeVectorLine])
@alg.input(type=alg.SINK, name='OUTPUT_NODI', label="nodi")
@alg.input(type=alg.SINK, name='OUTPUT_GRAFO', label="grafo")
@alg.output(type=str, name="OUT", label="Output")
def processAlgorithm(instance, parameters, context, feedback, inputs):
    """
    Algoritm to extract elevation on DTM from linestring paths at specified measure step
    """

    def aggiungi_nodo(nuovo_nodo):
        for i,nodo in enumerate(lista_nodi):
            if nodo.compare(nuovo_nodo):
                return i
        lista_nodi.append(nuovo_nodo)
        return len(lista_nodi)-1

    linee_layer = instance.parameterAsSource(parameters, "INPUT_LINEE", context)

    grafo_fields=QgsFields()
    grafo_fields.append(QgsField("rif_id", QVariant.Int))
    grafo_fields.append(QgsField("in_id", QVariant.Int))
    grafo_fields.append(QgsField("out_id", QVariant.Int))
    
    (grafo_sink, grafo_dest_id) = instance.parameterAsSink(parameters, "OUTPUT_GRAFO", context, grafo_fields, QgsWkbTypes.LineString, linee_layer.sourceCrs())
    
    nodi_fields = QgsFields()
    nodi_fields.append(QgsField("nodo_id", QVariant.Int))
    (nodi_sink, nodi_dest_id) = instance.parameterAsSink(parameters, "OUTPUT_NODI", context, nodi_fields, QgsWkbTypes.Point, linee_layer.sourceCrs())
    
    i = 0
    n = linee_layer.featureCount()
    lista_nodi = []
    feedback.pushInfo("Individuazione dei vertici degli archi del grafo ...")

    for k,feature in enumerate(linee_layer.getFeatures()):
        feedback.setProgress(int(100*i/n))
        i += 1
        lista_vertici = feature.geometry().asPolyline()
        grafo_feature = QgsFeature()
        attributi =[feature.id()]
        grafo_feature.setGeometry(feature.geometry())
        for campo, estremo in ({1:lista_vertici[0],2:lista_vertici[-1]}).items():
            id_nodo = aggiungi_nodo(estremo)
            attributi.append(id_nodo)
        grafo_feature.setAttributes(attributi)
        grafo_sink.addFeature(grafo_feature, QgsFeatureSink.FastInsert)

    i = 0
    n = len(lista_nodi)
    feedback.pushInfo("Creazione dei nodi ...")

    for i, nodo in enumerate(lista_nodi):
        feedback.setProgress(int(100*i/n))
        nodo_feature = QgsFeature()
        nodo_feature.setAttributes([i])
        nodo_feature.setGeometry(QgsGeometry.fromPointXY(nodo))
        nodi_sink.addFeature(nodo_feature, QgsFeatureSink.FastInsert)

    return {"OUTPUT_NODI": nodi_dest_id, "OUTPUT_GRAFO": grafo_dest_id}
