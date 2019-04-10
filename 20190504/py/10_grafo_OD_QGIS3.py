# -*- coding: utf-8 -*-

from PyQt5.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterRasterLayer,
                       QgsProcessingParameterNumber,
                       QgsProcessingParameterFeatureSink,
                       QgsFields,QgsField,QgsFeature,QgsGeometry, QgsWkbTypes, QgsRaster)

class GRAFOProcessingAlgorithm(QgsProcessingAlgorithm):
    """
    base algoritm class
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT_GRAFO = 'OUTPUT_GRAFO'
    OUTPUT_NODI = 'OUTPUT_NODI'
    INPUT_LINEE = 'INPUT_LINEE'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return GRAFOProcessingAlgorithm()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'origine_destinazione'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Crea grafo origine/destinazione')

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr('customscripts')

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'customscripts'

    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("Example algorithm short description")

    def initAlgorithm(self, config=None):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        self.addParameter(QgsProcessingParameterFeatureSource(
            self.INPUT_LINEE,
            self.tr("Linee"),[QgsProcessing.TypeVectorLine]))
            
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT_NODI,
            self.tr("Output nodi"),
            QgsProcessing.TypeVectorPoint))
            
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT_GRAFO,
            self.tr("Output grafo"),
            QgsProcessing.TypeVectorLine))
            
            
    def processAlgorithm(self, parameters, context, feedback):
        """
        Algoritm to extract elevation on DTM from linestring paths at specified measure step
        """
    
        def aggiungi_nodo(nuovo_nodo):
            for i,nodo in enumerate(lista_nodi):
                if nodo.compare(nuovo_nodo):
                    return i
            lista_nodi.append(nuovo_nodo)
            return len(lista_nodi)-1
    
        linee_layer = self.parameterAsSource(parameters, "INPUT_LINEE", context)
    
        grafo_fields=QgsFields()
        grafo_fields.append(QgsField("rif_id", QVariant.Int))
        grafo_fields.append(QgsField("in_id", QVariant.Int))
        grafo_fields.append(QgsField("out_id", QVariant.Int))
        
        (grafo_sink, grafo_dest_id) = self.parameterAsSink(parameters, "OUTPUT_GRAFO", context, grafo_fields, QgsWkbTypes.LineString, linee_layer.sourceCrs())
        
        nodi_fields = QgsFields()
        nodi_fields.append(QgsField("nodo_id", QVariant.Int))
        (nodi_sink, nodi_dest_id) = self.parameterAsSink(parameters, "OUTPUT_NODI", context, nodi_fields, QgsWkbTypes.Point, linee_layer.sourceCrs())
        
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