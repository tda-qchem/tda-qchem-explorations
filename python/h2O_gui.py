# state file generated using paraview version 5.10.1

# uncomment the following three lines to ensure this script works in future versions
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1377, 1172]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [-0.22030878067016602, 0.4097743034362793, 0.11670923233032227]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [6.230807115384138, -5.253755904378376, 24.109201480155342]
renderView1.CameraFocalPoint = [-0.46801266295389826, 1.4829689348131574, 0.49311110301857103]
renderView1.CameraViewUp = [-0.05917613516243776, -0.9642564891728971, -0.25827816035274015]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 7.971894106692482
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1377, 1172)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
start_data_allvti = XMLImageDataReader(registrationName='start_data_all.vti', FileName=['data/H2O_ED_basins/vti/start_data_all.vti'])
start_data_allvti.CellArrayStatus = ['vtkGhostType']
start_data_allvti.PointArrayStatus = ['rho', 'vtkValidPointMask', 'vtkGhostType']
start_data_allvti.TimeArray = 'None'

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(registrationName='TTKTopologicalSimplificationByPersistence1', Input=start_data_allvti)
tTKTopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'rho']

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=tTKTopologicalSimplificationByPersistence1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'rho']
tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'rho']
tTKMorseSmaleComplex1.AscendingSegmentation = 0
tTKMorseSmaleComplex1.DescendingSegmentation = 0
tTKMorseSmaleComplex1.MorseSmaleComplexSegmentation = 0

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother1', Input=OutputPort(tTKMorseSmaleComplex1_1,1))
tTKGeometrySmoother1.IterationNumber = 1000
tTKGeometrySmoother1.InputMaskField = ['CELLS', 'SeparatrixType']

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=tTKGeometrySmoother1)
threshold1.Scalars = ['CELLS', 'SeparatrixType']
threshold1.LowerThreshold = 2.0
threshold1.UpperThreshold = 2.0

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=threshold1)
threshold2.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=start_data_allvti)
contour1.ContourBy = ['POINTS', 'rho']
contour1.Isosurfaces = [0.1]
contour1.PointMergeMethod = 'Uniform Binning'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'rho'
rhoLUT = GetColorTransferFunction('rho')
rhoLUT.RGBPoints = [0.10000000149011612, 0.0, 0.129412, 0.584314, 0.10000763088464737, 0.917647, 0.941176, 0.788235, 0.10001526027917862, 0.0, 0.431373, 0.0]
rhoLUT.ColorSpace = 'RGB'
rhoLUT.AboveRangeColor = [1.0, 1.0, 1.0]
rhoLUT.NanColor = [0.0, 0.0, 0.0]
rhoLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.LookupTable = rhoLUT
contour1Display.Opacity = 0.2
contour1Display.Specular = 1.0
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleArray = 'rho'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.016778768599033357
contour1Display.SelectScaleArray = 'rho'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'rho'
contour1Display.GaussianRadius = 0.0008389384299516678
contour1Display.SetScaleArray = ['POINTS', 'rho']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'rho']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.SelectInputVectors = ['POINTS', 'Normals']
contour1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [86.28901672363281, 0.0, 0.5, 0.0, 86.30464172363281, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [86.28901672363281, 0.0, 0.5, 0.0, 86.30464172363281, 1.0, 0.5, 0.0]

# show data from tTKMorseSmaleComplex1
tTKMorseSmaleComplex1Display = Show(tTKMorseSmaleComplex1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'CellDimension'
cellDimensionLUT = GetColorTransferFunction('CellDimension')
cellDimensionLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5000000000000013, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
cellDimensionLUT.ColorSpace = 'RGB'
cellDimensionLUT.AboveRangeColor = [1.0, 1.0, 1.0]
cellDimensionLUT.NanColor = [0.0, 0.0, 0.0]
cellDimensionLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKMorseSmaleComplex1Display.Representation = 'Surface'
tTKMorseSmaleComplex1Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.LookupTable = cellDimensionLUT
tTKMorseSmaleComplex1Display.PointSize = 30.0
tTKMorseSmaleComplex1Display.RenderPointsAsSpheres = 1
tTKMorseSmaleComplex1Display.Specular = 1.0
tTKMorseSmaleComplex1Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1Display.ScaleFactor = 1.0422608375549316
tTKMorseSmaleComplex1Display.SelectScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GaussianRadius = 0.05211304187774658
tTKMorseSmaleComplex1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKMorseSmaleComplex1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# find source
tTKMorseSmaleComplex1_2 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_2
tTKMorseSmaleComplex1_2Display = Show(OutputPort(tTKMorseSmaleComplex1_2, 2), renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKMorseSmaleComplex1_2Display.Representation = 'Surface'
tTKMorseSmaleComplex1_2Display.ColorArrayName = ['POINTS', '']
tTKMorseSmaleComplex1_2Display.Specular = 1.0
tTKMorseSmaleComplex1_2Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1_2Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1_2Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1_2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_2Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1_2Display.ScaleFactor = -0.2
tTKMorseSmaleComplex1_2Display.SelectScaleArray = 'None'
tTKMorseSmaleComplex1_2Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1_2Display.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex1_2Display.GaussianRadius = -0.01
tTKMorseSmaleComplex1_2Display.SetScaleArray = ['POINTS', '']
tTKMorseSmaleComplex1_2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_2Display.OpacityArray = ['POINTS', '']
tTKMorseSmaleComplex1_2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1_2Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1_2Display.SelectInputVectors = ['POINTS', '']
tTKMorseSmaleComplex1_2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1_2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# show data from tTKGeometrySmoother1
tTKGeometrySmoother1Display = Show(tTKGeometrySmoother1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'SeparatrixType'
separatrixTypeLUT = GetColorTransferFunction('SeparatrixType')
separatrixTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.0002441406250009, 0.917647, 0.941176, 0.788235, 2.00048828125, 0.0, 0.431373, 0.0]
separatrixTypeLUT.ColorSpace = 'RGB'
separatrixTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
separatrixTypeLUT.NanColor = [0.0, 0.0, 0.0]
separatrixTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKGeometrySmoother1Display.Representation = 'Surface'
tTKGeometrySmoother1Display.ColorArrayName = ['CELLS', 'SeparatrixType']
tTKGeometrySmoother1Display.LookupTable = separatrixTypeLUT
tTKGeometrySmoother1Display.Opacity = 0.3
tTKGeometrySmoother1Display.LineWidth = 5.0
tTKGeometrySmoother1Display.RenderLinesAsTubes = 1
tTKGeometrySmoother1Display.Specular = 1.0
tTKGeometrySmoother1Display.SelectTCoordArray = 'None'
tTKGeometrySmoother1Display.SelectNormalArray = 'None'
tTKGeometrySmoother1Display.SelectTangentArray = 'None'
tTKGeometrySmoother1Display.OSPRayScaleArray = 'CellDimension'
tTKGeometrySmoother1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother1Display.ScaleFactor = 1.0422608375549316
tTKGeometrySmoother1Display.SelectScaleArray = 'SeparatrixType'
tTKGeometrySmoother1Display.GlyphType = 'Arrow'
tTKGeometrySmoother1Display.GlyphTableIndexArray = 'SeparatrixType'
tTKGeometrySmoother1Display.GaussianRadius = 0.05211304187774658
tTKGeometrySmoother1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKGeometrySmoother1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKGeometrySmoother1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother1Display.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKGeometrySmoother1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# show data from threshold2
threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'SeparatrixType'
separatrixTypePWF = GetOpacityTransferFunction('SeparatrixType')
separatrixTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 2.00048828125, 1.0, 0.5, 0.0]
separatrixTypePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = ['CELLS', 'SeparatrixType']
threshold2Display.LookupTable = separatrixTypeLUT
threshold2Display.LineWidth = 15.0
threshold2Display.RenderLinesAsTubes = 1
threshold2Display.Specular = 1.0
threshold2Display.SelectTCoordArray = 'None'
threshold2Display.SelectNormalArray = 'None'
threshold2Display.SelectTangentArray = 'None'
threshold2Display.OSPRayScaleArray = 'CellDimension'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'None'
threshold2Display.ScaleFactor = 0.27903045415878297
threshold2Display.SelectScaleArray = 'SeparatrixType'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'SeparatrixType'
threshold2Display.GaussianRadius = 0.013951522707939147
threshold2Display.SetScaleArray = ['POINTS', 'CellDimension']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'CellDimension']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityFunction = separatrixTypePWF
threshold2Display.ScalarOpacityUnitDistance = 0.41469775523114205
threshold2Display.OpacityArrayName = ['CELLS', 'SeparatrixType']
threshold2Display.SelectInputVectors = ['POINTS', 'CellDimension']
threshold2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'rho'
rhoPWF = GetOpacityTransferFunction('rho')
rhoPWF.Points = [0.10000000149011612, 0.0, 0.5, 0.0, 0.10001526027917862, 1.0, 0.5, 0.0]
rhoPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(threshold2)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')