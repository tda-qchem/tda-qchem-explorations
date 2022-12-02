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
renderView1.ViewSize = [1377, 564]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.7683676928830725, 20.161084688194897, 4.338376735358313]
renderView1.CameraFocalPoint = [0.0, -1e-20, 0.0]
renderView1.CameraViewUp = [-0.004325922102125578, -0.2102106696757141, 0.9776465418301516]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 7.820080520075376
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView10 = CreateView('RenderView')
renderView10.ViewSize = [683, 563]
renderView10.AxesGrid = 'GridAxes3DActor'
renderView10.OrientationAxesVisibility = 0
renderView10.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView10.StereoType = 'Crystal Eyes'
renderView10.CameraPosition = [-0.48610571363436184, 21.14156439337225, 5.938616165787505]
renderView10.CameraFocalPoint = [-0.02574804975648673, -2.7045705873596004, -1.4561547569497613]
renderView10.CameraViewUp = [-0.0029610111817006558, -0.2962398448439609, 0.9551089920734742]
renderView10.CameraFocalDisk = 1.0
renderView10.CameraParallelScale = 7.820080520075376
renderView10.UseColorPaletteForBackground = 0
renderView10.Background = [1.0, 1.0, 1.0]
renderView10.BackEnd = 'OSPRay raycaster'
renderView10.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [684, 563]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.OrientationAxesVisibility = 0
renderView2.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [0.0, 20.636890206955403, 0.0]
renderView2.CameraFocalPoint = [0.0, -1e-20, 0.0]
renderView2.CameraViewUp = [0.0, 0.0, 1.0]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 7.820080520075376
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.ViewSize = [683, 563]
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.OrientationAxesVisibility = 0
renderView3.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraPosition = [0.0, 20.636890206955403, 0.0]
renderView3.CameraFocalPoint = [0.0, -1e-20, 0.0]
renderView3.CameraViewUp = [0.0, 0.0, 1.0]
renderView3.CameraFocalDisk = 1.0
renderView3.CameraParallelScale = 7.820080520075376
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView4 = CreateView('RenderView')
renderView4.ViewSize = [684, 1172]
renderView4.AxesGrid = 'GridAxes3DActor'
renderView4.OrientationAxesVisibility = 0
renderView4.CenterOfRotation = [0.0, 1.9661997103305215, 0.0]
renderView4.StereoType = 'Crystal Eyes'
renderView4.CameraPosition = [0.0, 42.89490414558687, 0.0]
renderView4.CameraFocalPoint = [0.0, 1.9661997103305215, 0.0]
renderView4.CameraViewUp = [0.0, 0.0, 1.0]
renderView4.CameraFocalDisk = 1.0
renderView4.CameraParallelScale = 10.593128199216359
renderView4.UseColorPaletteForBackground = 0
renderView4.Background = [1.0, 1.0, 1.0]
renderView4.BackEnd = 'OSPRay raycaster'
renderView4.Shadows = 1
renderView4.AmbientSamples = 4
renderView4.SamplesPerPixel = 4
renderView4.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView5 = CreateView('RenderView')
renderView5.ViewSize = [683, 564]
renderView5.AxesGrid = 'GridAxes3DActor'
renderView5.OrientationAxesVisibility = 0
renderView5.CenterOfRotation = [0.7125580310821533, 0.0, 0.0]
renderView5.StereoType = 'Crystal Eyes'
renderView5.CameraPosition = [1.8567215175885559, 6.49947558261868, 0.09456697029865793]
renderView5.CameraFocalPoint = [1.0041010884536372, -0.037442552411962905, -0.030513653439580894]
renderView5.CameraViewUp = [0.015946314931483005, -0.021207660170597074, 0.9996479131125091]
renderView5.CameraFocalDisk = 1.0
renderView5.CameraParallelScale = 11.743275661962203
renderView5.UseColorPaletteForBackground = 0
renderView5.Background = [1.0, 1.0, 1.0]
renderView5.BackEnd = 'OSPRay raycaster'
renderView5.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView6 = CreateView('RenderView')
renderView6.ViewSize = [683, 563]
renderView6.AxesGrid = 'GridAxes3DActor'
renderView6.OrientationAxesVisibility = 0
renderView6.StereoType = 'Crystal Eyes'
renderView6.CameraPosition = [-0.23141696055091165, 11.655813358411772, 0.2895578809896814]
renderView6.CameraFocalPoint = [-0.5359189544348181, 0.01715308415166948, -0.09482796784114833]
renderView6.CameraViewUp = [0.003848458683573176, -0.03310897599412297, 0.9994443381571491]
renderView6.CameraFocalDisk = 1.0
renderView6.CameraParallelScale = 7.820080520075376
renderView6.UseColorPaletteForBackground = 0
renderView6.Background = [1.0, 1.0, 1.0]
renderView6.BackEnd = 'OSPRay raycaster'
renderView6.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView7 = CreateView('RenderView')
renderView7.ViewSize = [684, 564]
renderView7.AxesGrid = 'GridAxes3DActor'
renderView7.OrientationAxesVisibility = 0
renderView7.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView7.StereoType = 'Crystal Eyes'
renderView7.CameraPosition = [-0.48610571363436184, 21.14156439337225, 5.938616165787505]
renderView7.CameraFocalPoint = [-0.02574804975648673, -2.7045705873596004, -1.4561547569497613]
renderView7.CameraViewUp = [-0.0029610111817006558, -0.2962398448439609, 0.9551089920734742]
renderView7.CameraFocalDisk = 1.0
renderView7.CameraParallelScale = 7.820080520075376
renderView7.UseColorPaletteForBackground = 0
renderView7.Background = [1.0, 1.0, 1.0]
renderView7.BackEnd = 'OSPRay raycaster'
renderView7.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView8 = CreateView('RenderView')
renderView8.ViewSize = [683, 564]
renderView8.AxesGrid = 'GridAxes3DActor'
renderView8.OrientationAxesVisibility = 0
renderView8.CenterOfRotation = [0.49936618737029903, 0.5000009768371569, 0.0]
renderView8.StereoType = 'Crystal Eyes'
renderView8.CameraPosition = [0.49936618737029903, 0.5000009768371569, 2.2564602931646442]
renderView8.CameraFocalPoint = [0.49936618737029903, 0.5000009768371569, 0.0]
renderView8.CameraFocalDisk = 1.0
renderView8.CameraParallelScale = 0.7066580270502391
renderView8.UseColorPaletteForBackground = 0
renderView8.Background = [1.0, 1.0, 1.0]
renderView8.BackEnd = 'OSPRay raycaster'
renderView8.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView9 = CreateView('RenderView')
renderView9.ViewSize = [684, 563]
renderView9.AxesGrid = 'GridAxes3DActor'
renderView9.OrientationAxesVisibility = 0
renderView9.CenterOfRotation = [0.0, -1e-20, 0.0]
renderView9.StereoType = 'Crystal Eyes'
renderView9.CameraPosition = [-0.48610571363436184, 21.14156439337225, 5.938616165787505]
renderView9.CameraFocalPoint = [-0.02574804975648673, -2.7045705873596004, -1.4561547569497613]
renderView9.CameraViewUp = [-0.0029610111817006558, -0.2962398448439609, 0.9551089920734742]
renderView9.CameraFocalDisk = 1.0
renderView9.CameraParallelScale = 7.820080520075376
renderView9.UseColorPaletteForBackground = 0
renderView9.Background = [1.0, 1.0, 1.0]
renderView9.BackEnd = 'OSPRay raycaster'
renderView9.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Input Data'
inputData = CreateLayout(name='Input Data')
inputData.SplitHorizontal(0, 0.500000)
inputData.AssignView(1, renderView4)
inputData.SplitVertical(2, 0.500000)
inputData.AssignView(5, renderView5)
inputData.AssignView(6, renderView6)
inputData.SetSize(1368, 1172)

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.SplitHorizontal(2, 0.500000)
layout1.AssignView(5, renderView2)
layout1.AssignView(6, renderView3)
layout1.SetSize(1377, 1128)

# create new layout object 'Topological Analysis'
topologicalAnalysis = CreateLayout(name='Topological Analysis')
topologicalAnalysis.SplitHorizontal(0, 0.500000)
topologicalAnalysis.SplitVertical(1, 0.500000)
topologicalAnalysis.AssignView(3, renderView7)
topologicalAnalysis.AssignView(4, renderView9)
topologicalAnalysis.SplitVertical(2, 0.500000)
topologicalAnalysis.AssignView(5, renderView8)
topologicalAnalysis.AssignView(6, renderView10)
topologicalAnalysis.SetSize(1368, 1128)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView8)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Image Data Reader'
start_data_omega_bzvti = XMLImageDataReader(registrationName='start_data_omega_bz.vti', FileName=['data/LiH_MICD/vti/start_data_omega_bz.vti'])
start_data_omega_bzvti.CellArrayStatus = ['vtkGhostType']
start_data_omega_bzvti.PointArrayStatus = ['bz_wz', 'omega_bz', 'vtkValidPointMask', 'vtkGhostType']
start_data_omega_bzvti.TimeArray = 'None'

# create a new 'TTK DiscreteGradient'
tTKDiscreteGradient1 = TTKDiscreteGradient(registrationName='TTKDiscreteGradient1', Input=start_data_omega_bzvti)
tTKDiscreteGradient1.ScalarField = ['POINTS', 'omega_bz']
tTKDiscreteGradient1.OffsetField = ['POINTS', 'bz_wz']
tTKDiscreteGradient1.ComputeGradientGlyphs = 0

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=start_data_omega_bzvti)
calculator1.ResultArrayName = 'oppositeOmega'
calculator1.Function = '-omega_bz'

# create a new 'Contour'
contour2 = Contour(registrationName='Contour2', Input=start_data_omega_bzvti)
contour2.ContourBy = ['POINTS', 'omega_bz']
contour2.Isosurfaces = [0.8]
contour2.PointMergeMethod = 'Uniform Binning'

# create a new 'Connectivity'
connectivity2 = Connectivity(registrationName='Connectivity2', Input=contour2)

# create a new 'Threshold'
threshold6 = Threshold(registrationName='Threshold6', Input=connectivity2)
threshold6.Scalars = ['POINTS', 'RegionId']
threshold6.LowerThreshold = 1.0
threshold6.UpperThreshold = 1.0

# create a new 'Contour'
contour4 = Contour(registrationName='Contour4', Input=start_data_omega_bzvti)
contour4.ContourBy = ['POINTS', 'omega_bz']
contour4.Isosurfaces = [0.996]
contour4.PointMergeMethod = 'Uniform Binning'

# create a new 'Threshold'
threshold8 = Threshold(registrationName='Threshold8', Input=connectivity2)
threshold8.Scalars = ['POINTS', 'RegionId']

# create a new 'TTK PersistentGenerators'
tTKPersistentGenerators1 = TTKPersistentGenerators(registrationName='TTKPersistentGenerators1', Input=calculator1)
tTKPersistentGenerators1.ScalarField = ['POINTS', 'oppositeOmega']
tTKPersistentGenerators1.InputOffsetField = ['POINTS', 'oppositeOmega']

# create a new 'TTK ScalarFieldNormalizer'
tTKScalarFieldNormalizer1 = TTKScalarFieldNormalizer(registrationName='TTKScalarFieldNormalizer1', Input=start_data_omega_bzvti)
tTKScalarFieldNormalizer1.ScalarField = ['POINTS', 'omega_bz']

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=tTKScalarFieldNormalizer1)
tTKPersistenceDiagram1.ScalarField = ['POINTS', 'omega_bz']
tTKPersistenceDiagram1.InputOffsetField = ['POINTS', 'bz_wz']

# create a new 'Contour'
contour3 = Contour(registrationName='Contour3', Input=start_data_omega_bzvti)
contour3.ContourBy = ['POINTS', 'omega_bz']
contour3.Isosurfaces = [0.92]
contour3.PointMergeMethod = 'Uniform Binning'

# create a new 'Connectivity'
connectivity3 = Connectivity(registrationName='Connectivity3', Input=contour3)

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=start_data_omega_bzvti)
contour1.ContourBy = ['POINTS', 'omega_bz']
contour1.Isosurfaces = [0.5]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Connectivity'
connectivity1 = Connectivity(registrationName='Connectivity1', Input=contour1)

# create a new 'Threshold'
threshold4 = Threshold(registrationName='Threshold4', Input=connectivity1)
threshold4.Scalars = ['POINTS', 'RegionId']
threshold4.LowerThreshold = 2.0
threshold4.UpperThreshold = 2.0

# create a new 'Threshold'
threshold10 = Threshold(registrationName='Threshold10', Input=tTKPersistenceDiagram1)
threshold10.Scalars = ['CELLS', 'Persistence']
threshold10.LowerThreshold = 0.3
threshold10.UpperThreshold = 1.9999999999999998

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints3 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints3', Input=threshold10)
tTKIcospheresFromPoints3.Radius = 0.025

# create a new 'Threshold'
threshold7 = Threshold(registrationName='Threshold7', Input=connectivity3)
threshold7.Scalars = ['POINTS', 'RegionId']
threshold7.LowerThreshold = 1.0
threshold7.UpperThreshold = 2.0

# create a new 'Extract Surface'
extractSurface3 = ExtractSurface(registrationName='ExtractSurface3', Input=threshold10)

# create a new 'Threshold'
threshold9 = Threshold(registrationName='Threshold9', Input=tTKPersistenceDiagram1)
threshold9.Scalars = ['CELLS', 'PairIdentifier']
threshold9.LowerThreshold = -1.0
threshold9.UpperThreshold = -0.1

# create a new 'Extract Surface'
extractSurface2 = ExtractSurface(registrationName='ExtractSurface2', Input=threshold9)

# create a new 'Tube'
tube2 = Tube(registrationName='Tube2', Input=extractSurface2)
tube2.Scalars = ['POINTS', 'CriticalType']
tube2.Vectors = ['POINTS', 'Coordinates']
tube2.Radius = 0.01

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=tTKPersistentGenerators1)
threshold1.Scalars = ['CELLS', 'Persistence']
threshold1.LowerThreshold = 0.5
threshold1.UpperThreshold = 0.8493308367608376

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother2 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother2', Input=threshold1)
tTKGeometrySmoother2.IterationNumber = 2
tTKGeometrySmoother2.InputMaskField = ['POINTS', '']

# create a new 'Threshold'
threshold5 = Threshold(registrationName='Threshold5', Input=connectivity1)
threshold5.Scalars = ['POINTS', 'RegionId']

# create a new 'TTK TopologicalSimplificationByPersistence'
tTKTopologicalSimplificationByPersistence1 = TTKTopologicalSimplificationByPersistence(registrationName='TTKTopologicalSimplificationByPersistence1', Input=tTKScalarFieldNormalizer1)
tTKTopologicalSimplificationByPersistence1.InputArray = ['POINTS', 'omega_bz']
tTKTopologicalSimplificationByPersistence1.PersistenceThreshold = 0.3

# create a new 'TTK MorseSmaleComplex'
tTKMorseSmaleComplex1 = TTKMorseSmaleComplex(registrationName='TTKMorseSmaleComplex1', Input=tTKTopologicalSimplificationByPersistence1)
tTKMorseSmaleComplex1.ScalarField = ['POINTS', 'omega_bz']
tTKMorseSmaleComplex1.OffsetField = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1.AscendingSegmentation = 0
tTKMorseSmaleComplex1.DescendingSegmentation = 0
tTKMorseSmaleComplex1.MorseSmaleComplexSegmentation = 0
tTKMorseSmaleComplex1.ReturnSaddleConnectors = 1
tTKMorseSmaleComplex1.SaddleConnectorsPersistenceThreshold = 0.3

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints2', Input=tTKMorseSmaleComplex1)
tTKIcospheresFromPoints2.Radius = 0.175

# find source
tTKMorseSmaleComplex1_1 = FindSource('TTKMorseSmaleComplex1')

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother1', Input=OutputPort(tTKMorseSmaleComplex1_1,1))
tTKGeometrySmoother1.IterationNumber = 1000
tTKGeometrySmoother1.InputMaskField = ['CELLS', 'SeparatrixType']

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=tTKGeometrySmoother1)

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=extractSurface1)
tube1.Scalars = ['POINTS', 'CellDimension']
tube1.Vectors = ['POINTS', '1']
tube1.Radius = 0.05

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=tTKGeometrySmoother1)
threshold2.Scalars = ['CELLS', 'SeparatrixType']
threshold2.LowerThreshold = 2.0
threshold2.UpperThreshold = 2.0

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=threshold2)
threshold3.Scalars = ['CELLS', 'NumberOfCriticalPointsOnBoundary']
threshold3.LowerThreshold = 1.0
threshold3.UpperThreshold = 1.0

# create a new 'Tube'
tube3 = Tube(registrationName='Tube3', Input=extractSurface3)
tube3.Scalars = ['POINTS', 'CriticalType']
tube3.Vectors = ['POINTS', 'Coordinates']
tube3.Radius = 0.01

# create a new 'Threshold'
threshold11 = Threshold(registrationName='Threshold11', Input=tube3)
threshold11.Scalars = ['CELLS', 'PairIdentifier']
threshold11.LowerThreshold = -0.1
threshold11.UpperThreshold = 190.0

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints1', Input=tTKDiscreteGradient1)
tTKIcospheresFromPoints1.Radius = 0.175

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'omega_bz'
omega_bzLUT = GetColorTransferFunction('omega_bz')
omega_bzLUT.RGBPoints = [0.4000000059604645, 0.0, 0.129412, 0.584314, 0.6985610276460648, 0.917647, 0.941176, 0.788235, 0.997122049331665, 0.0, 0.431373, 0.0]
omega_bzLUT.ColorSpace = 'RGB'
omega_bzLUT.AboveRangeColor = [1.0, 1.0, 1.0]
omega_bzLUT.NanColor = [0.0, 0.0, 0.0]
omega_bzLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', '']
contour1Display.LookupTable = omega_bzLUT
contour1Display.Opacity = 0.3
contour1Display.Specular = 1.0
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'Normals'
contour1Display.SelectTangentArray = 'None'
contour1Display.EdgeColor = [0.0, 0.0, 0.0]
contour1Display.OSPRayScaleArray = 'omega_bz'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.846682643890381
contour1Display.SelectScaleArray = 'omega_bz'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'omega_bz'
contour1Display.GaussianRadius = 0.04233413219451904
contour1Display.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'omega_bz']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'
contour1Display.SelectInputVectors = ['POINTS', 'Normals']
contour1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [0.6000000238418579, 0.0, 0.5, 0.0, 0.6001220941543579, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.6000000238418579, 0.0, 0.5, 0.0, 0.6001220941543579, 1.0, 0.5, 0.0]

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
tTKMorseSmaleComplex1Display.PointSize = 20.0
tTKMorseSmaleComplex1Display.LineWidth = 10.0
tTKMorseSmaleComplex1Display.RenderLinesAsTubes = 1
tTKMorseSmaleComplex1Display.RenderPointsAsSpheres = 1
tTKMorseSmaleComplex1Display.Specular = 1.0
tTKMorseSmaleComplex1Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKMorseSmaleComplex1Display.OSPRayScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1Display.ScaleFactor = 0.8466827869415283
tTKMorseSmaleComplex1Display.SelectScaleArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1Display.GlyphTableIndexArray = 'CellDimension'
tTKMorseSmaleComplex1Display.GaussianRadius = 0.042334139347076416
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
tTKMorseSmaleComplex1_2Display.EdgeColor = [0.0, 0.0, 0.0]
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

# find source
tTKMorseSmaleComplex1_3 = FindSource('TTKMorseSmaleComplex1')

# show data from tTKMorseSmaleComplex1_3
tTKMorseSmaleComplex1_3Display = Show(OutputPort(tTKMorseSmaleComplex1_3, 3), renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
tTKMorseSmaleComplex1_3Display.Representation = 'Outline'
tTKMorseSmaleComplex1_3Display.ColorArrayName = ['POINTS', '']
tTKMorseSmaleComplex1_3Display.SelectTCoordArray = 'None'
tTKMorseSmaleComplex1_3Display.SelectNormalArray = 'None'
tTKMorseSmaleComplex1_3Display.SelectTangentArray = 'None'
tTKMorseSmaleComplex1_3Display.OSPRayScaleArray = 'bz_wz'
tTKMorseSmaleComplex1_3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.SelectOrientationVectors = 'None'
tTKMorseSmaleComplex1_3Display.ScaleFactor = 1.006182531816462
tTKMorseSmaleComplex1_3Display.SelectScaleArray = 'None'
tTKMorseSmaleComplex1_3Display.GlyphType = 'Arrow'
tTKMorseSmaleComplex1_3Display.GlyphTableIndexArray = 'None'
tTKMorseSmaleComplex1_3Display.GaussianRadius = 0.050309126590823094
tTKMorseSmaleComplex1_3Display.SetScaleArray = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.OpacityArray = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKMorseSmaleComplex1_3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKMorseSmaleComplex1_3Display.PolarAxes = 'PolarAxesRepresentation'
tTKMorseSmaleComplex1_3Display.ScalarOpacityUnitDistance = 0.12315087617612483
tTKMorseSmaleComplex1_3Display.OpacityArrayName = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.SliceFunction = 'Plane'
tTKMorseSmaleComplex1_3Display.Slice = 63
tTKMorseSmaleComplex1_3Display.SelectInputVectors = ['POINTS', 'bz_wz']
tTKMorseSmaleComplex1_3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKMorseSmaleComplex1_3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKMorseSmaleComplex1_3Display.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKMorseSmaleComplex1_3Display.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

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
tTKGeometrySmoother1Display.LineWidth = 5.0
tTKGeometrySmoother1Display.RenderLinesAsTubes = 1
tTKGeometrySmoother1Display.Specular = 1.0
tTKGeometrySmoother1Display.SelectTCoordArray = 'None'
tTKGeometrySmoother1Display.SelectNormalArray = 'None'
tTKGeometrySmoother1Display.SelectTangentArray = 'None'
tTKGeometrySmoother1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKGeometrySmoother1Display.OSPRayScaleArray = 'CellDimension'
tTKGeometrySmoother1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother1Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother1Display.ScaleFactor = 0.9348782539367676
tTKGeometrySmoother1Display.SelectScaleArray = 'SeparatrixType'
tTKGeometrySmoother1Display.GlyphType = 'Arrow'
tTKGeometrySmoother1Display.GlyphTableIndexArray = 'SeparatrixType'
tTKGeometrySmoother1Display.GaussianRadius = 0.04674391269683838
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

# ----------------------------------------------------------------
# setup the visualization in view 'renderView10'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay = Show(start_data_omega_bzvti, renderView10, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay.Representation = 'Outline'
start_data_omega_bzvtiDisplay.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay.ColorArrayName = [None, '']
start_data_omega_bzvtiDisplay.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay.Slice = 63
start_data_omega_bzvtiDisplay.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_1 = Show(contour1, renderView10, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_1.Representation = 'Surface'
contour1Display_1.ColorArrayName = ['POINTS', '']
contour1Display_1.Opacity = 0.2
contour1Display_1.Specular = 1.0
contour1Display_1.SelectTCoordArray = 'None'
contour1Display_1.SelectNormalArray = 'Normals'
contour1Display_1.SelectTangentArray = 'None'
contour1Display_1.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_1.OSPRayScaleArray = 'omega_bz'
contour1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_1.SelectOrientationVectors = 'None'
contour1Display_1.ScaleFactor = 0.8636709690093994
contour1Display_1.SelectScaleArray = 'omega_bz'
contour1Display_1.GlyphType = 'Arrow'
contour1Display_1.GlyphTableIndexArray = 'omega_bz'
contour1Display_1.GaussianRadius = 0.04318354845046997
contour1Display_1.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_1.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_1.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_1.PolarAxes = 'PolarAxesRepresentation'
contour1Display_1.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_1.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_1.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from tTKIcospheresFromPoints2
tTKIcospheresFromPoints2Display = Show(tTKIcospheresFromPoints2, renderView10, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints2Display.Representation = 'Surface'
tTKIcospheresFromPoints2Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display.LookupTable = cellDimensionLUT
tTKIcospheresFromPoints2Display.Specular = 1.0
tTKIcospheresFromPoints2Display.SelectTCoordArray = 'None'
tTKIcospheresFromPoints2Display.SelectNormalArray = 'Normals'
tTKIcospheresFromPoints2Display.SelectTangentArray = 'None'
tTKIcospheresFromPoints2Display.EdgeColor = [0.0, 0.0, 0.0]
tTKIcospheresFromPoints2Display.OSPRayScaleArray = 'CellDimension'
tTKIcospheresFromPoints2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display.SelectOrientationVectors = 'None'
tTKIcospheresFromPoints2Display.ScaleFactor = 0.866682767868042
tTKIcospheresFromPoints2Display.SelectScaleArray = 'CellDimension'
tTKIcospheresFromPoints2Display.GlyphType = 'Arrow'
tTKIcospheresFromPoints2Display.GlyphTableIndexArray = 'CellDimension'
tTKIcospheresFromPoints2Display.GaussianRadius = 0.043334138393402104
tTKIcospheresFromPoints2Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display.OpacityArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKIcospheresFromPoints2Display.PolarAxes = 'PolarAxesRepresentation'
tTKIcospheresFromPoints2Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKIcospheresFromPoints2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIcospheresFromPoints2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIcospheresFromPoints2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# show data from tube1
tube1Display = Show(tube1, renderView10, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = ['CELLS', 'SeparatrixType']
tube1Display.LookupTable = separatrixTypeLUT
tube1Display.Specular = 1.0
tube1Display.SelectTCoordArray = 'None'
tube1Display.SelectNormalArray = 'TubeNormals'
tube1Display.SelectTangentArray = 'None'
tube1Display.EdgeColor = [0.0, 0.0, 0.0]
tube1Display.OSPRayScaleArray = 'CellDimension'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'None'
tube1Display.ScaleFactor = 0.863616418838501
tube1Display.SelectScaleArray = 'SeparatrixType'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'SeparatrixType'
tube1Display.GaussianRadius = 0.04318082094192505
tube1Display.SetScaleArray = ['POINTS', 'CellDimension']
tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
tube1Display.OpacityArray = ['POINTS', 'CellDimension']
tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
tube1Display.DataAxesGrid = 'GridAxesRepresentation'
tube1Display.PolarAxes = 'PolarAxesRepresentation'
tube1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tube1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_1 = Show(start_data_omega_bzvti, renderView2, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_1.Representation = 'Outline'
start_data_omega_bzvtiDisplay_1.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_1.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_1.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_1.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_1.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_1.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_1.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_1.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_1.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_1.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_1.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_1.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_1.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_1.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_1.Slice = 63
start_data_omega_bzvtiDisplay_1.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_1.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_1.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_2 = Show(contour1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_2.Representation = 'Surface'
contour1Display_2.ColorArrayName = ['POINTS', '']
contour1Display_2.LookupTable = omega_bzLUT
contour1Display_2.Opacity = 0.2
contour1Display_2.Specular = 1.0
contour1Display_2.SelectTCoordArray = 'None'
contour1Display_2.SelectNormalArray = 'Normals'
contour1Display_2.SelectTangentArray = 'None'
contour1Display_2.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_2.OSPRayScaleArray = 'omega_bz'
contour1Display_2.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_2.SelectOrientationVectors = 'None'
contour1Display_2.ScaleFactor = 0.8636709690093994
contour1Display_2.SelectScaleArray = 'omega_bz'
contour1Display_2.GlyphType = 'Arrow'
contour1Display_2.GlyphTableIndexArray = 'omega_bz'
contour1Display_2.GaussianRadius = 0.04318354845046997
contour1Display_2.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_2.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_2.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_2.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_2.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_2.PolarAxes = 'PolarAxesRepresentation'
contour1Display_2.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_2.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_2.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_2.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from tTKGeometrySmoother2
tTKGeometrySmoother2Display = Show(tTKGeometrySmoother2, renderView2, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Persistence'
persistenceLUT = GetColorTransferFunction('Persistence')
persistenceLUT.RGBPoints = [7.237523249419703e-06, 0.0, 0.129412, 0.584314, 0.42473007516535743, 0.917647, 0.941176, 0.788235, 0.8494529128074646, 0.0, 0.431373, 0.0]
persistenceLUT.ColorSpace = 'RGB'
persistenceLUT.AboveRangeColor = [1.0, 1.0, 1.0]
persistenceLUT.NanColor = [0.0, 0.0, 0.0]
persistenceLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Persistence'
persistencePWF = GetOpacityTransferFunction('Persistence')
persistencePWF.Points = [7.237523249419703e-06, 0.0, 0.5, 0.0, 0.8494529128074646, 1.0, 0.5, 0.0]
persistencePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
tTKGeometrySmoother2Display.Representation = 'Surface'
tTKGeometrySmoother2Display.ColorArrayName = ['CELLS', 'Persistence']
tTKGeometrySmoother2Display.LookupTable = persistenceLUT
tTKGeometrySmoother2Display.LineWidth = 10.0
tTKGeometrySmoother2Display.RenderLinesAsTubes = 1
tTKGeometrySmoother2Display.Specular = 1.0
tTKGeometrySmoother2Display.SelectTCoordArray = 'None'
tTKGeometrySmoother2Display.SelectNormalArray = 'None'
tTKGeometrySmoother2Display.SelectTangentArray = 'None'
tTKGeometrySmoother2Display.OSPRayScaleArray = 'oppositeOmega'
tTKGeometrySmoother2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.SelectOrientationVectors = 'None'
tTKGeometrySmoother2Display.ScaleFactor = 0.07141872048377991
tTKGeometrySmoother2Display.SelectScaleArray = 'None'
tTKGeometrySmoother2Display.GlyphType = 'Arrow'
tTKGeometrySmoother2Display.GlyphTableIndexArray = 'None'
tTKGeometrySmoother2Display.GaussianRadius = 0.0035709360241889952
tTKGeometrySmoother2Display.SetScaleArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.OpacityArray = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKGeometrySmoother2Display.DataAxesGrid = 'GridAxesRepresentation'
tTKGeometrySmoother2Display.PolarAxes = 'PolarAxesRepresentation'
tTKGeometrySmoother2Display.ScalarOpacityFunction = persistencePWF
tTKGeometrySmoother2Display.ScalarOpacityUnitDistance = 0.21744076418518754
tTKGeometrySmoother2Display.OpacityArrayName = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.SelectInputVectors = ['POINTS', 'oppositeOmega']
tTKGeometrySmoother2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKGeometrySmoother2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKGeometrySmoother2Display.ScaleTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKGeometrySmoother2Display.OpacityTransferFunction.Points = [-0.9751526647579255, 0.0, 0.5, 0.0, -0.9056711359213363, 1.0, 0.5, 0.0]

# show data from tTKPersistentGenerators1
tTKPersistentGenerators1Display = Show(tTKPersistentGenerators1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKPersistentGenerators1Display.Representation = 'Surface'
tTKPersistentGenerators1Display.ColorArrayName = [None, '']
tTKPersistentGenerators1Display.Specular = 1.0
tTKPersistentGenerators1Display.SelectTCoordArray = 'None'
tTKPersistentGenerators1Display.SelectNormalArray = 'None'
tTKPersistentGenerators1Display.SelectTangentArray = 'None'
tTKPersistentGenerators1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKPersistentGenerators1Display.OSPRayScaleArray = 'oppositeOmega'
tTKPersistentGenerators1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPersistentGenerators1Display.SelectOrientationVectors = 'None'
tTKPersistentGenerators1Display.ScaleFactor = 1.0061824798583985
tTKPersistentGenerators1Display.SelectScaleArray = 'None'
tTKPersistentGenerators1Display.GlyphType = 'Arrow'
tTKPersistentGenerators1Display.GlyphTableIndexArray = 'None'
tTKPersistentGenerators1Display.GaussianRadius = 0.050309123992919924
tTKPersistentGenerators1Display.SetScaleArray = ['POINTS', 'oppositeOmega']
tTKPersistentGenerators1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPersistentGenerators1Display.OpacityArray = ['POINTS', 'oppositeOmega']
tTKPersistentGenerators1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPersistentGenerators1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPersistentGenerators1Display.PolarAxes = 'PolarAxesRepresentation'
tTKPersistentGenerators1Display.SelectInputVectors = ['POINTS', 'oppositeOmega']
tTKPersistentGenerators1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKPersistentGenerators1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPersistentGenerators1Display.ScaleTransferFunction.Points = [-0.9949202085539145, 0.0, 0.5, 0.0, -0.0064376340156840905, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPersistentGenerators1Display.OpacityTransferFunction.Points = [-0.9949202085539145, 0.0, 0.5, 0.0, -0.0064376340156840905, 1.0, 0.5, 0.0]

# hide data in view
Hide(tTKPersistentGenerators1, renderView2)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView3'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_2 = Show(start_data_omega_bzvti, renderView3, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_2.Representation = 'Outline'
start_data_omega_bzvtiDisplay_2.ColorArrayName = ['POINTS', '']
start_data_omega_bzvtiDisplay_2.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_2.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_2.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_2.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_2.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_2.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_2.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_2.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_2.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_2.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_2.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_2.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_2.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_2.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_2.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_2.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_2.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_2.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_2.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_2.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_2.Slice = 63
start_data_omega_bzvtiDisplay_2.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_2.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_2.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_2.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_2.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_3 = Show(contour1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_3.Representation = 'Surface'
contour1Display_3.ColorArrayName = ['POINTS', '']
contour1Display_3.LookupTable = omega_bzLUT
contour1Display_3.Opacity = 0.1
contour1Display_3.Specular = 1.0
contour1Display_3.SelectTCoordArray = 'None'
contour1Display_3.SelectNormalArray = 'Normals'
contour1Display_3.SelectTangentArray = 'None'
contour1Display_3.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_3.OSPRayScaleArray = 'omega_bz'
contour1Display_3.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_3.SelectOrientationVectors = 'None'
contour1Display_3.ScaleFactor = 0.8636709690093994
contour1Display_3.SelectScaleArray = 'omega_bz'
contour1Display_3.GlyphType = 'Arrow'
contour1Display_3.GlyphTableIndexArray = 'omega_bz'
contour1Display_3.GaussianRadius = 0.04318354845046997
contour1Display_3.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_3.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_3.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_3.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_3.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_3.PolarAxes = 'PolarAxesRepresentation'
contour1Display_3.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_3.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_3.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_3.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_3.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from threshold3
threshold3Display = Show(threshold3, renderView3, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'SeparatrixType'
separatrixTypePWF = GetOpacityTransferFunction('SeparatrixType')
separatrixTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 2.00048828125, 1.0, 0.5, 0.0]
separatrixTypePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'
threshold3Display.ColorArrayName = ['CELLS', 'SeparatrixType']
threshold3Display.LookupTable = separatrixTypeLUT
threshold3Display.LineWidth = 10.0
threshold3Display.RenderLinesAsTubes = 1
threshold3Display.Specular = 1.0
threshold3Display.SelectTCoordArray = 'None'
threshold3Display.SelectNormalArray = 'None'
threshold3Display.SelectTangentArray = 'None'
threshold3Display.OSPRayScaleArray = 'CellDimension'
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'None'
threshold3Display.ScaleFactor = 0.8466827869415283
threshold3Display.SelectScaleArray = 'SeparatrixType'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GlyphTableIndexArray = 'SeparatrixType'
threshold3Display.GaussianRadius = 0.042334139347076416
threshold3Display.SetScaleArray = ['POINTS', 'CellDimension']
threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display.OpacityArray = ['POINTS', 'CellDimension']
threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display.PolarAxes = 'PolarAxesRepresentation'
threshold3Display.ScalarOpacityFunction = separatrixTypePWF
threshold3Display.ScalarOpacityUnitDistance = 0.9099565514149196
threshold3Display.OpacityArrayName = ['CELLS', 'SeparatrixType']
threshold3Display.SelectInputVectors = ['POINTS', 'CellDimension']
threshold3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView4'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_3 = Show(start_data_omega_bzvti, renderView4, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_3.Representation = 'Outline'
start_data_omega_bzvtiDisplay_3.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_3.ColorArrayName = [None, '']
start_data_omega_bzvtiDisplay_3.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_3.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_3.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_3.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_3.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_3.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_3.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_3.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_3.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_3.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_3.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_3.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_3.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_3.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_3.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_3.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_3.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_3.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_3.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_3.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_3.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_3.Slice = 63
start_data_omega_bzvtiDisplay_3.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_3.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_3.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_3.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_3.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_4 = Show(contour1, renderView4, 'GeometryRepresentation')

# get color transfer function/color map for 'bz_wz'
bz_wzLUT = GetColorTransferFunction('bz_wz')
bz_wzLUT.RGBPoints = [-0.36186845055807093, 0.0, 0.129412, 0.584314, 3.788039026700919, 0.917647, 0.941176, 0.788235, 7.937946503959902, 0.0, 0.431373, 0.0]
bz_wzLUT.ColorSpace = 'RGB'
bz_wzLUT.AboveRangeColor = [1.0, 1.0, 1.0]
bz_wzLUT.NanColor = [0.0, 0.0, 0.0]
bz_wzLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display_4.Representation = 'Surface'
contour1Display_4.ColorArrayName = ['POINTS', 'bz_wz']
contour1Display_4.LookupTable = bz_wzLUT
contour1Display_4.Specular = 1.0
contour1Display_4.SelectTCoordArray = 'None'
contour1Display_4.SelectNormalArray = 'Normals'
contour1Display_4.SelectTangentArray = 'None'
contour1Display_4.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_4.OSPRayScaleArray = 'omega_bz'
contour1Display_4.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_4.SelectOrientationVectors = 'None'
contour1Display_4.ScaleFactor = 0.8636709690093994
contour1Display_4.SelectScaleArray = 'omega_bz'
contour1Display_4.GlyphType = 'Arrow'
contour1Display_4.GlyphTableIndexArray = 'omega_bz'
contour1Display_4.GaussianRadius = 0.04318354845046997
contour1Display_4.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_4.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_4.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_4.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_4.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_4.PolarAxes = 'PolarAxesRepresentation'
contour1Display_4.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_4.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_4.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_4.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_4.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView5'
# ----------------------------------------------------------------

# show data from contour1
contour1Display_5 = Show(contour1, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_5.Representation = 'Surface'
contour1Display_5.ColorArrayName = ['POINTS', 'bz_wz']
contour1Display_5.LookupTable = bz_wzLUT
contour1Display_5.Specular = 1.0
contour1Display_5.SelectTCoordArray = 'None'
contour1Display_5.SelectNormalArray = 'Normals'
contour1Display_5.SelectTangentArray = 'None'
contour1Display_5.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_5.OSPRayScaleArray = 'omega_bz'
contour1Display_5.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_5.SelectOrientationVectors = 'None'
contour1Display_5.ScaleFactor = 0.8636709690093994
contour1Display_5.SelectScaleArray = 'omega_bz'
contour1Display_5.GlyphType = 'Arrow'
contour1Display_5.GlyphTableIndexArray = 'omega_bz'
contour1Display_5.GaussianRadius = 0.04318354845046997
contour1Display_5.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_5.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_5.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_5.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_5.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_5.PolarAxes = 'PolarAxesRepresentation'
contour1Display_5.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_5.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_5.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_5.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_5.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_4 = Show(start_data_omega_bzvti, renderView5, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_4.Representation = 'Outline'
start_data_omega_bzvtiDisplay_4.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_4.ColorArrayName = [None, '']
start_data_omega_bzvtiDisplay_4.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_4.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_4.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_4.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_4.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_4.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_4.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_4.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_4.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_4.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_4.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_4.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_4.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_4.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_4.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_4.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_4.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_4.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_4.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_4.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_4.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_4.Slice = 63
start_data_omega_bzvtiDisplay_4.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_4.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_4.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_4.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_4.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from connectivity1
connectivity1Display = Show(connectivity1, renderView5, 'GeometryRepresentation')

# get color transfer function/color map for 'RegionId'
regionIdLUT = GetColorTransferFunction('RegionId')
regionIdLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5000000000000013, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
regionIdLUT.ColorSpace = 'RGB'
regionIdLUT.AboveRangeColor = [1.0, 1.0, 1.0]
regionIdLUT.NanColor = [0.0, 0.0, 0.0]
regionIdLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
connectivity1Display.Representation = 'Surface'
connectivity1Display.ColorArrayName = ['POINTS', 'RegionId']
connectivity1Display.LookupTable = regionIdLUT
connectivity1Display.Specular = 1.0
connectivity1Display.SelectTCoordArray = 'None'
connectivity1Display.SelectNormalArray = 'Normals'
connectivity1Display.SelectTangentArray = 'None'
connectivity1Display.EdgeColor = [0.0, 0.0, 0.0]
connectivity1Display.OSPRayScaleArray = 'RegionId'
connectivity1Display.OSPRayScaleFunction = 'PiecewiseFunction'
connectivity1Display.SelectOrientationVectors = 'None'
connectivity1Display.ScaleFactor = 0.8636709690093994
connectivity1Display.SelectScaleArray = 'RegionId'
connectivity1Display.GlyphType = 'Arrow'
connectivity1Display.GlyphTableIndexArray = 'RegionId'
connectivity1Display.GaussianRadius = 0.04318354845046997
connectivity1Display.SetScaleArray = ['POINTS', 'RegionId']
connectivity1Display.ScaleTransferFunction = 'PiecewiseFunction'
connectivity1Display.OpacityArray = ['POINTS', 'RegionId']
connectivity1Display.OpacityTransferFunction = 'PiecewiseFunction'
connectivity1Display.DataAxesGrid = 'GridAxesRepresentation'
connectivity1Display.PolarAxes = 'PolarAxesRepresentation'
connectivity1Display.SelectInputVectors = ['POINTS', 'Normals']
connectivity1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
connectivity1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
connectivity1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
connectivity1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# show data from threshold4
threshold4Display = Show(threshold4, renderView5, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'bz_wz'
bz_wzPWF = GetOpacityTransferFunction('bz_wz')
bz_wzPWF.Points = [-0.36186845055807093, 0.0, 0.5, 0.0, 7.937946503959902, 1.0, 0.5, 0.0]
bz_wzPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold4Display.Representation = 'Surface'
threshold4Display.ColorArrayName = ['POINTS', 'bz_wz']
threshold4Display.LookupTable = bz_wzLUT
threshold4Display.Opacity = 0.3
threshold4Display.Specular = 1.0
threshold4Display.SelectTCoordArray = 'None'
threshold4Display.SelectNormalArray = 'Normals'
threshold4Display.SelectTangentArray = 'None'
threshold4Display.OSPRayScaleArray = 'RegionId'
threshold4Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold4Display.SelectOrientationVectors = 'None'
threshold4Display.ScaleFactor = 0.3055371522903443
threshold4Display.SelectScaleArray = 'RegionId'
threshold4Display.GlyphType = 'Arrow'
threshold4Display.GlyphTableIndexArray = 'RegionId'
threshold4Display.GaussianRadius = 0.015276857614517213
threshold4Display.SetScaleArray = ['POINTS', 'RegionId']
threshold4Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold4Display.OpacityArray = ['POINTS', 'RegionId']
threshold4Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold4Display.DataAxesGrid = 'GridAxesRepresentation'
threshold4Display.PolarAxes = 'PolarAxesRepresentation'
threshold4Display.ScalarOpacityFunction = bz_wzPWF
threshold4Display.ScalarOpacityUnitDistance = 0.1864963582339875
threshold4Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold4Display.SelectInputVectors = ['POINTS', 'Normals']
threshold4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold4Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold4Display.ScaleTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 2.00048828125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold4Display.OpacityTransferFunction.Points = [2.0, 0.0, 0.5, 0.0, 2.00048828125, 1.0, 0.5, 0.0]

# show data from contour2
contour2Display = Show(contour2, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
contour2Display.Representation = 'Surface'
contour2Display.ColorArrayName = ['POINTS', 'omega_bz']
contour2Display.LookupTable = omega_bzLUT
contour2Display.Specular = 1.0
contour2Display.SelectTCoordArray = 'None'
contour2Display.SelectNormalArray = 'Normals'
contour2Display.SelectTangentArray = 'None'
contour2Display.EdgeColor = [0.0, 0.0, 0.0]
contour2Display.OSPRayScaleArray = 'omega_bz'
contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour2Display.SelectOrientationVectors = 'None'
contour2Display.ScaleFactor = 0.8636709690093994
contour2Display.SelectScaleArray = 'omega_bz'
contour2Display.GlyphType = 'Arrow'
contour2Display.GlyphTableIndexArray = 'omega_bz'
contour2Display.GaussianRadius = 0.04318354845046997
contour2Display.SetScaleArray = ['POINTS', 'omega_bz']
contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
contour2Display.OpacityArray = ['POINTS', 'omega_bz']
contour2Display.OpacityTransferFunction = 'PiecewiseFunction'
contour2Display.DataAxesGrid = 'GridAxesRepresentation'
contour2Display.PolarAxes = 'PolarAxesRepresentation'
contour2Display.SelectInputVectors = ['POINTS', 'Normals']
contour2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2Display.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2Display.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from connectivity2
connectivity2Display = Show(connectivity2, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
connectivity2Display.Representation = 'Surface'
connectivity2Display.ColorArrayName = ['POINTS', 'RegionId']
connectivity2Display.LookupTable = regionIdLUT
connectivity2Display.Specular = 1.0
connectivity2Display.SelectTCoordArray = 'None'
connectivity2Display.SelectNormalArray = 'Normals'
connectivity2Display.SelectTangentArray = 'None'
connectivity2Display.EdgeColor = [0.0, 0.0, 0.0]
connectivity2Display.OSPRayScaleArray = 'RegionId'
connectivity2Display.OSPRayScaleFunction = 'PiecewiseFunction'
connectivity2Display.SelectOrientationVectors = 'None'
connectivity2Display.ScaleFactor = 0.846682643890381
connectivity2Display.SelectScaleArray = 'RegionId'
connectivity2Display.GlyphType = 'Arrow'
connectivity2Display.GlyphTableIndexArray = 'RegionId'
connectivity2Display.GaussianRadius = 0.04233413219451904
connectivity2Display.SetScaleArray = ['POINTS', 'RegionId']
connectivity2Display.ScaleTransferFunction = 'PiecewiseFunction'
connectivity2Display.OpacityArray = ['POINTS', 'RegionId']
connectivity2Display.OpacityTransferFunction = 'PiecewiseFunction'
connectivity2Display.DataAxesGrid = 'GridAxesRepresentation'
connectivity2Display.PolarAxes = 'PolarAxesRepresentation'
connectivity2Display.SelectInputVectors = ['POINTS', 'Normals']
connectivity2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
connectivity2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# show data from threshold6
threshold6Display = Show(threshold6, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold6Display.Representation = 'Surface'
threshold6Display.ColorArrayName = ['POINTS', 'bz_wz']
threshold6Display.LookupTable = bz_wzLUT
threshold6Display.Opacity = 0.3
threshold6Display.Specular = 1.0
threshold6Display.SelectTCoordArray = 'None'
threshold6Display.SelectNormalArray = 'Normals'
threshold6Display.SelectTangentArray = 'None'
threshold6Display.OSPRayScaleArray = 'RegionId'
threshold6Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold6Display.SelectOrientationVectors = 'None'
threshold6Display.ScaleFactor = 0.270881986618042
threshold6Display.SelectScaleArray = 'RegionId'
threshold6Display.GlyphType = 'Arrow'
threshold6Display.GlyphTableIndexArray = 'RegionId'
threshold6Display.GaussianRadius = 0.0135440993309021
threshold6Display.SetScaleArray = ['POINTS', 'RegionId']
threshold6Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold6Display.OpacityArray = ['POINTS', 'RegionId']
threshold6Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold6Display.DataAxesGrid = 'GridAxesRepresentation'
threshold6Display.PolarAxes = 'PolarAxesRepresentation'
threshold6Display.ScalarOpacityFunction = bz_wzPWF
threshold6Display.ScalarOpacityUnitDistance = 0.19660327886133
threshold6Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold6Display.SelectInputVectors = ['POINTS', 'Normals']
threshold6Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold6Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold6Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold6Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 1.000244140625, 1.0, 0.5, 0.0]

# show data from contour3
contour3Display = Show(contour3, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
contour3Display.Representation = 'Surface'
contour3Display.ColorArrayName = ['POINTS', 'omega_bz']
contour3Display.LookupTable = omega_bzLUT
contour3Display.Specular = 1.0
contour3Display.SelectTCoordArray = 'None'
contour3Display.SelectNormalArray = 'Normals'
contour3Display.SelectTangentArray = 'None'
contour3Display.EdgeColor = [0.0, 0.0, 0.0]
contour3Display.OSPRayScaleArray = 'omega_bz'
contour3Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour3Display.SelectOrientationVectors = 'None'
contour3Display.ScaleFactor = 0.846682643890381
contour3Display.SelectScaleArray = 'omega_bz'
contour3Display.GlyphType = 'Arrow'
contour3Display.GlyphTableIndexArray = 'omega_bz'
contour3Display.GaussianRadius = 0.04233413219451904
contour3Display.SetScaleArray = ['POINTS', 'omega_bz']
contour3Display.ScaleTransferFunction = 'PiecewiseFunction'
contour3Display.OpacityArray = ['POINTS', 'omega_bz']
contour3Display.OpacityTransferFunction = 'PiecewiseFunction'
contour3Display.DataAxesGrid = 'GridAxesRepresentation'
contour3Display.PolarAxes = 'PolarAxesRepresentation'
contour3Display.SelectInputVectors = ['POINTS', 'Normals']
contour3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour3Display.ScaleTransferFunction.Points = [0.949999988079071, 0.0, 0.5, 0.0, 0.950122058391571, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour3Display.OpacityTransferFunction.Points = [0.949999988079071, 0.0, 0.5, 0.0, 0.950122058391571, 1.0, 0.5, 0.0]

# show data from connectivity3
connectivity3Display = Show(connectivity3, renderView5, 'GeometryRepresentation')

# trace defaults for the display properties.
connectivity3Display.Representation = 'Surface'
connectivity3Display.ColorArrayName = ['POINTS', 'RegionId']
connectivity3Display.LookupTable = regionIdLUT
connectivity3Display.Specular = 1.0
connectivity3Display.SelectTCoordArray = 'None'
connectivity3Display.SelectNormalArray = 'Normals'
connectivity3Display.SelectTangentArray = 'None'
connectivity3Display.EdgeColor = [0.0, 0.0, 0.0]
connectivity3Display.OSPRayScaleArray = 'RegionId'
connectivity3Display.OSPRayScaleFunction = 'PiecewiseFunction'
connectivity3Display.SelectOrientationVectors = 'None'
connectivity3Display.ScaleFactor = 0.846682643890381
connectivity3Display.SelectScaleArray = 'RegionId'
connectivity3Display.GlyphType = 'Arrow'
connectivity3Display.GlyphTableIndexArray = 'RegionId'
connectivity3Display.GaussianRadius = 0.04233413219451904
connectivity3Display.SetScaleArray = ['POINTS', 'RegionId']
connectivity3Display.ScaleTransferFunction = 'PiecewiseFunction'
connectivity3Display.OpacityArray = ['POINTS', 'RegionId']
connectivity3Display.OpacityTransferFunction = 'PiecewiseFunction'
connectivity3Display.DataAxesGrid = 'GridAxesRepresentation'
connectivity3Display.PolarAxes = 'PolarAxesRepresentation'
connectivity3Display.SelectInputVectors = ['POINTS', 'Normals']
connectivity3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
connectivity3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
connectivity3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
connectivity3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# show data from threshold7
threshold7Display = Show(threshold7, renderView5, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold7Display.Representation = 'Surface'
threshold7Display.ColorArrayName = ['POINTS', 'bz_wz']
threshold7Display.LookupTable = bz_wzLUT
threshold7Display.Specular = 1.0
threshold7Display.SelectTCoordArray = 'None'
threshold7Display.SelectNormalArray = 'Normals'
threshold7Display.SelectTangentArray = 'None'
threshold7Display.OSPRayScaleArray = 'RegionId'
threshold7Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold7Display.SelectOrientationVectors = 'None'
threshold7Display.ScaleFactor = 0.2549871921539307
threshold7Display.SelectScaleArray = 'RegionId'
threshold7Display.GlyphType = 'Arrow'
threshold7Display.GlyphTableIndexArray = 'RegionId'
threshold7Display.GaussianRadius = 0.012749359607696534
threshold7Display.SetScaleArray = ['POINTS', 'RegionId']
threshold7Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold7Display.OpacityArray = ['POINTS', 'RegionId']
threshold7Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold7Display.DataAxesGrid = 'GridAxesRepresentation'
threshold7Display.PolarAxes = 'PolarAxesRepresentation'
threshold7Display.ScalarOpacityFunction = bz_wzPWF
threshold7Display.ScalarOpacityUnitDistance = 0.2430388853433246
threshold7Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold7Display.SelectInputVectors = ['POINTS', 'Normals']
threshold7Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold7Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold7Display.ScaleTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold7Display.OpacityTransferFunction.Points = [1.0, 0.0, 0.5, 0.0, 2.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(contour1, renderView5)

# hide data in view
Hide(connectivity1, renderView5)

# hide data in view
Hide(contour2, renderView5)

# hide data in view
Hide(connectivity2, renderView5)

# hide data in view
Hide(contour3, renderView5)

# hide data in view
Hide(connectivity3, renderView5)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView6'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_5 = Show(start_data_omega_bzvti, renderView6, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_5.Representation = 'Outline'
start_data_omega_bzvtiDisplay_5.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_5.ColorArrayName = [None, '']
start_data_omega_bzvtiDisplay_5.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_5.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_5.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_5.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_5.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_5.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_5.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_5.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_5.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_5.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_5.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_5.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_5.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_5.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_5.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_5.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_5.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_5.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_5.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_5.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_5.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_5.Slice = 63
start_data_omega_bzvtiDisplay_5.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_5.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_5.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_5.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_5.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from threshold5
threshold5Display = Show(threshold5, renderView6, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold5Display.Representation = 'Surface'
threshold5Display.ColorArrayName = ['POINTS', 'bz_wz']
threshold5Display.LookupTable = bz_wzLUT
threshold5Display.Opacity = 0.3
threshold5Display.Specular = 1.0
threshold5Display.SelectTCoordArray = 'None'
threshold5Display.SelectNormalArray = 'Normals'
threshold5Display.SelectTangentArray = 'None'
threshold5Display.OSPRayScaleArray = 'RegionId'
threshold5Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold5Display.SelectOrientationVectors = 'None'
threshold5Display.ScaleFactor = 0.846682643890381
threshold5Display.SelectScaleArray = 'RegionId'
threshold5Display.GlyphType = 'Arrow'
threshold5Display.GlyphTableIndexArray = 'RegionId'
threshold5Display.GaussianRadius = 0.04233413219451904
threshold5Display.SetScaleArray = ['POINTS', 'RegionId']
threshold5Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold5Display.OpacityArray = ['POINTS', 'RegionId']
threshold5Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold5Display.DataAxesGrid = 'GridAxesRepresentation'
threshold5Display.PolarAxes = 'PolarAxesRepresentation'
threshold5Display.ScalarOpacityFunction = bz_wzPWF
threshold5Display.ScalarOpacityUnitDistance = 0.2873884165867302
threshold5Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold5Display.SelectInputVectors = ['POINTS', 'Normals']
threshold5Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold5Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold5Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold5Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from threshold8
threshold8Display = Show(threshold8, renderView6, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'RegionId'
regionIdPWF = GetOpacityTransferFunction('RegionId')
regionIdPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
regionIdPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold8Display.Representation = 'Surface'
threshold8Display.ColorArrayName = ['POINTS', 'RegionId']
threshold8Display.LookupTable = regionIdLUT
threshold8Display.Opacity = 0.3
threshold8Display.Specular = 1.0
threshold8Display.SelectTCoordArray = 'None'
threshold8Display.SelectNormalArray = 'Normals'
threshold8Display.SelectTangentArray = 'None'
threshold8Display.OSPRayScaleArray = 'RegionId'
threshold8Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold8Display.SelectOrientationVectors = 'None'
threshold8Display.ScaleFactor = 0.846682643890381
threshold8Display.SelectScaleArray = 'RegionId'
threshold8Display.GlyphType = 'Arrow'
threshold8Display.GlyphTableIndexArray = 'RegionId'
threshold8Display.GaussianRadius = 0.04233413219451904
threshold8Display.SetScaleArray = ['POINTS', 'RegionId']
threshold8Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold8Display.OpacityArray = ['POINTS', 'RegionId']
threshold8Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold8Display.DataAxesGrid = 'GridAxesRepresentation'
threshold8Display.PolarAxes = 'PolarAxesRepresentation'
threshold8Display.ScalarOpacityFunction = regionIdPWF
threshold8Display.ScalarOpacityUnitDistance = 0.3316778671322185
threshold8Display.OpacityArrayName = ['POINTS', 'RegionId']
threshold8Display.SelectInputVectors = ['POINTS', 'Normals']
threshold8Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold8Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# show data from contour4
contour4Display = Show(contour4, renderView6, 'GeometryRepresentation')

# trace defaults for the display properties.
contour4Display.Representation = 'Surface'
contour4Display.ColorArrayName = ['POINTS', 'bz_wz']
contour4Display.LookupTable = bz_wzLUT
contour4Display.Specular = 1.0
contour4Display.SelectTCoordArray = 'None'
contour4Display.SelectNormalArray = 'Normals'
contour4Display.SelectTangentArray = 'None'
contour4Display.EdgeColor = [0.0, 0.0, 0.0]
contour4Display.OSPRayScaleArray = 'omega_bz'
contour4Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour4Display.SelectOrientationVectors = 'None'
contour4Display.ScaleFactor = 0.846682643890381
contour4Display.SelectScaleArray = 'omega_bz'
contour4Display.GlyphType = 'Arrow'
contour4Display.GlyphTableIndexArray = 'omega_bz'
contour4Display.GaussianRadius = 0.04233413219451904
contour4Display.SetScaleArray = ['POINTS', 'omega_bz']
contour4Display.ScaleTransferFunction = 'PiecewiseFunction'
contour4Display.OpacityArray = ['POINTS', 'omega_bz']
contour4Display.OpacityTransferFunction = 'PiecewiseFunction'
contour4Display.DataAxesGrid = 'GridAxesRepresentation'
contour4Display.PolarAxes = 'PolarAxesRepresentation'
contour4Display.SelectInputVectors = ['POINTS', 'Normals']
contour4Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour4Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour4Display.ScaleTransferFunction.Points = [0.9900000095367432, 0.0, 0.5, 0.0, 0.9901220798492432, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour4Display.OpacityTransferFunction.Points = [0.9900000095367432, 0.0, 0.5, 0.0, 0.9901220798492432, 1.0, 0.5, 0.0]

# hide data in view
Hide(start_data_omega_bzvti, renderView6)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView7'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_6 = Show(start_data_omega_bzvti, renderView7, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_6.Representation = 'Outline'
start_data_omega_bzvtiDisplay_6.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_6.ColorArrayName = [None, '']
start_data_omega_bzvtiDisplay_6.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_6.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_6.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_6.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_6.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_6.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_6.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_6.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_6.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_6.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_6.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_6.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_6.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_6.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_6.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_6.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_6.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_6.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_6.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_6.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_6.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_6.Slice = 63
start_data_omega_bzvtiDisplay_6.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_6.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_6.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_6.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_6.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_6 = Show(contour1, renderView7, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_6.Representation = 'Surface'
contour1Display_6.ColorArrayName = ['POINTS', '']
contour1Display_6.Opacity = 0.2
contour1Display_6.Specular = 1.0
contour1Display_6.SelectTCoordArray = 'None'
contour1Display_6.SelectNormalArray = 'Normals'
contour1Display_6.SelectTangentArray = 'None'
contour1Display_6.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_6.OSPRayScaleArray = 'omega_bz'
contour1Display_6.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_6.SelectOrientationVectors = 'None'
contour1Display_6.ScaleFactor = 0.8636709690093994
contour1Display_6.SelectScaleArray = 'omega_bz'
contour1Display_6.GlyphType = 'Arrow'
contour1Display_6.GlyphTableIndexArray = 'omega_bz'
contour1Display_6.GaussianRadius = 0.04318354845046997
contour1Display_6.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_6.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_6.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_6.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_6.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_6.PolarAxes = 'PolarAxesRepresentation'
contour1Display_6.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_6.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_6.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_6.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_6.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from tTKDiscreteGradient1
tTKDiscreteGradient1Display = Show(tTKDiscreteGradient1, renderView7, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKDiscreteGradient1Display.Representation = 'Surface'
tTKDiscreteGradient1Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKDiscreteGradient1Display.LookupTable = cellDimensionLUT
tTKDiscreteGradient1Display.Specular = 1.0
tTKDiscreteGradient1Display.SelectTCoordArray = 'None'
tTKDiscreteGradient1Display.SelectNormalArray = 'None'
tTKDiscreteGradient1Display.SelectTangentArray = 'None'
tTKDiscreteGradient1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKDiscreteGradient1Display.OSPRayScaleArray = 'CellDimension'
tTKDiscreteGradient1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKDiscreteGradient1Display.SelectOrientationVectors = 'None'
tTKDiscreteGradient1Display.ScaleFactor = 0.8466827392578126
tTKDiscreteGradient1Display.SelectScaleArray = 'CellDimension'
tTKDiscreteGradient1Display.GlyphType = 'Arrow'
tTKDiscreteGradient1Display.GlyphTableIndexArray = 'CellDimension'
tTKDiscreteGradient1Display.GaussianRadius = 0.04233413696289062
tTKDiscreteGradient1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKDiscreteGradient1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKDiscreteGradient1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKDiscreteGradient1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKDiscreteGradient1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKDiscreteGradient1Display.PolarAxes = 'PolarAxesRepresentation'
tTKDiscreteGradient1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKDiscreteGradient1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKDiscreteGradient1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKDiscreteGradient1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKDiscreteGradient1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# find source
tTKDiscreteGradient1_1 = FindSource('TTKDiscreteGradient1')

# show data from tTKDiscreteGradient1_1
tTKDiscreteGradient1_1Display = Show(OutputPort(tTKDiscreteGradient1_1, 1), renderView7, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKDiscreteGradient1_1Display.Representation = 'Surface'
tTKDiscreteGradient1_1Display.ColorArrayName = [None, '']
tTKDiscreteGradient1_1Display.Specular = 1.0
tTKDiscreteGradient1_1Display.SelectTCoordArray = 'None'
tTKDiscreteGradient1_1Display.SelectNormalArray = 'None'
tTKDiscreteGradient1_1Display.SelectTangentArray = 'None'
tTKDiscreteGradient1_1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKDiscreteGradient1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKDiscreteGradient1_1Display.SelectOrientationVectors = 'None'
tTKDiscreteGradient1_1Display.ScaleFactor = -0.2
tTKDiscreteGradient1_1Display.SelectScaleArray = 'None'
tTKDiscreteGradient1_1Display.GlyphType = 'Arrow'
tTKDiscreteGradient1_1Display.GlyphTableIndexArray = 'None'
tTKDiscreteGradient1_1Display.GaussianRadius = -0.01
tTKDiscreteGradient1_1Display.SetScaleArray = [None, '']
tTKDiscreteGradient1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKDiscreteGradient1_1Display.OpacityArray = [None, '']
tTKDiscreteGradient1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKDiscreteGradient1_1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKDiscreteGradient1_1Display.PolarAxes = 'PolarAxesRepresentation'
tTKDiscreteGradient1_1Display.SelectInputVectors = [None, '']
tTKDiscreteGradient1_1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKDiscreteGradient1_1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# show data from tTKIcospheresFromPoints1
tTKIcospheresFromPoints1Display = Show(tTKIcospheresFromPoints1, renderView7, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints1Display.Representation = 'Surface'
tTKIcospheresFromPoints1Display.ColorArrayName = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints1Display.LookupTable = cellDimensionLUT
tTKIcospheresFromPoints1Display.Specular = 1.0
tTKIcospheresFromPoints1Display.SelectTCoordArray = 'None'
tTKIcospheresFromPoints1Display.SelectNormalArray = 'Normals'
tTKIcospheresFromPoints1Display.SelectTangentArray = 'None'
tTKIcospheresFromPoints1Display.EdgeColor = [0.0, 0.0, 0.0]
tTKIcospheresFromPoints1Display.OSPRayScaleArray = 'CellDimension'
tTKIcospheresFromPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints1Display.SelectOrientationVectors = 'None'
tTKIcospheresFromPoints1Display.ScaleFactor = 1.0466827392578126
tTKIcospheresFromPoints1Display.SelectScaleArray = 'CellDimension'
tTKIcospheresFromPoints1Display.GlyphType = 'Arrow'
tTKIcospheresFromPoints1Display.GlyphTableIndexArray = 'CellDimension'
tTKIcospheresFromPoints1Display.GaussianRadius = 0.052334136962890625
tTKIcospheresFromPoints1Display.SetScaleArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints1Display.OpacityArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKIcospheresFromPoints1Display.PolarAxes = 'PolarAxesRepresentation'
tTKIcospheresFromPoints1Display.SelectInputVectors = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKIcospheresFromPoints1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIcospheresFromPoints1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIcospheresFromPoints1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# show data from extractSurface1
extractSurface1Display = Show(extractSurface1, renderView7, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'
extractSurface1Display.ColorArrayName = ['CELLS', 'SeparatrixType']
extractSurface1Display.LookupTable = separatrixTypeLUT
extractSurface1Display.Specular = 1.0
extractSurface1Display.SelectTCoordArray = 'None'
extractSurface1Display.SelectNormalArray = 'None'
extractSurface1Display.SelectTangentArray = 'None'
extractSurface1Display.EdgeColor = [0.0, 0.0, 0.0]
extractSurface1Display.OSPRayScaleArray = 'CellDimension'
extractSurface1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface1Display.SelectOrientationVectors = 'None'
extractSurface1Display.ScaleFactor = 0.8466827869415283
extractSurface1Display.SelectScaleArray = 'SeparatrixType'
extractSurface1Display.GlyphType = 'Arrow'
extractSurface1Display.GlyphTableIndexArray = 'SeparatrixType'
extractSurface1Display.GaussianRadius = 0.042334139347076416
extractSurface1Display.SetScaleArray = ['POINTS', 'CellDimension']
extractSurface1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface1Display.OpacityArray = ['POINTS', 'CellDimension']
extractSurface1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface1Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface1Display.SelectInputVectors = ['POINTS', 'CellDimension']
extractSurface1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractSurface1, renderView7)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView8'
# ----------------------------------------------------------------

# show data from tTKScalarFieldNormalizer1
tTKScalarFieldNormalizer1Display = Show(tTKScalarFieldNormalizer1, renderView8, 'UniformGridRepresentation')

# trace defaults for the display properties.
tTKScalarFieldNormalizer1Display.Representation = 'Outline'
tTKScalarFieldNormalizer1Display.ColorArrayName = [None, '']
tTKScalarFieldNormalizer1Display.SelectTCoordArray = 'None'
tTKScalarFieldNormalizer1Display.SelectNormalArray = 'None'
tTKScalarFieldNormalizer1Display.SelectTangentArray = 'None'
tTKScalarFieldNormalizer1Display.OSPRayScaleArray = 'bz_wz'
tTKScalarFieldNormalizer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKScalarFieldNormalizer1Display.SelectOrientationVectors = 'None'
tTKScalarFieldNormalizer1Display.ScaleFactor = 1.006182531816462
tTKScalarFieldNormalizer1Display.SelectScaleArray = 'None'
tTKScalarFieldNormalizer1Display.GlyphType = 'Arrow'
tTKScalarFieldNormalizer1Display.GlyphTableIndexArray = 'None'
tTKScalarFieldNormalizer1Display.GaussianRadius = 0.050309126590823094
tTKScalarFieldNormalizer1Display.SetScaleArray = ['POINTS', 'bz_wz']
tTKScalarFieldNormalizer1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKScalarFieldNormalizer1Display.OpacityArray = ['POINTS', 'bz_wz']
tTKScalarFieldNormalizer1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKScalarFieldNormalizer1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKScalarFieldNormalizer1Display.PolarAxes = 'PolarAxesRepresentation'
tTKScalarFieldNormalizer1Display.ScalarOpacityUnitDistance = 0.12315087617612483
tTKScalarFieldNormalizer1Display.OpacityArrayName = ['POINTS', 'bz_wz']
tTKScalarFieldNormalizer1Display.SliceFunction = 'Plane'
tTKScalarFieldNormalizer1Display.Slice = 63
tTKScalarFieldNormalizer1Display.SelectInputVectors = ['POINTS', 'bz_wz']
tTKScalarFieldNormalizer1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKScalarFieldNormalizer1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKScalarFieldNormalizer1Display.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKScalarFieldNormalizer1Display.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from tTKPersistenceDiagram1
tTKPersistenceDiagram1Display = Show(tTKPersistenceDiagram1, renderView8, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
tTKPersistenceDiagram1Display.Representation = 'Surface'
tTKPersistenceDiagram1Display.AmbientColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
tTKPersistenceDiagram1Display.ColorArrayName = [None, '']
tTKPersistenceDiagram1Display.DiffuseColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
tTKPersistenceDiagram1Display.Specular = 1.0
tTKPersistenceDiagram1Display.SelectTCoordArray = 'None'
tTKPersistenceDiagram1Display.SelectNormalArray = 'None'
tTKPersistenceDiagram1Display.SelectTangentArray = 'None'
tTKPersistenceDiagram1Display.OSPRayScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.SelectOrientationVectors = 'Coordinates'
tTKPersistenceDiagram1Display.ScaleFactor = 0.0999999953674319
tTKPersistenceDiagram1Display.SelectScaleArray = 'Coordinates'
tTKPersistenceDiagram1Display.GlyphType = 'Arrow'
tTKPersistenceDiagram1Display.GlyphTableIndexArray = 'Coordinates'
tTKPersistenceDiagram1Display.GaussianRadius = 0.004999999768371594
tTKPersistenceDiagram1Display.SetScaleArray = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.OpacityArray = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKPersistenceDiagram1Display.DataAxesGrid = 'GridAxesRepresentation'
tTKPersistenceDiagram1Display.PolarAxes = 'PolarAxesRepresentation'
tTKPersistenceDiagram1Display.ScalarOpacityUnitDistance = 0.2181304645116989
tTKPersistenceDiagram1Display.OpacityArrayName = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.SelectInputVectors = ['POINTS', 'Coordinates']
tTKPersistenceDiagram1Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKPersistenceDiagram1Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKPersistenceDiagram1Display.ScaleTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKPersistenceDiagram1Display.OpacityTransferFunction.Points = [-2.4164228439331055, 0.0, 0.5, 0.0, 5.030911922454834, 1.0, 0.5, 0.0]

# show data from threshold9
threshold9Display = Show(threshold9, renderView8, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'Coordinates'
coordinatesLUT = GetColorTransferFunction('Coordinates')
coordinatesLUT.RGBPoints = [0.06157508338376992, 0.0, 0.129412, 0.584314, 3.3183771414326744, 0.917647, 0.941176, 0.788235, 6.575179199481572, 0.0, 0.431373, 0.0]
coordinatesLUT.ColorSpace = 'RGB'
coordinatesLUT.AboveRangeColor = [1.0, 1.0, 1.0]
coordinatesLUT.NanColor = [0.0, 0.0, 0.0]
coordinatesLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'Coordinates'
coordinatesPWF = GetOpacityTransferFunction('Coordinates')
coordinatesPWF.Points = [0.06157508338376992, 0.0, 0.5, 0.0, 6.575179199481572, 1.0, 0.5, 0.0]
coordinatesPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
threshold9Display.Representation = 'Surface'
threshold9Display.ColorArrayName = ['POINTS', 'Coordinates']
threshold9Display.LookupTable = coordinatesLUT
threshold9Display.Specular = 1.0
threshold9Display.SelectTCoordArray = 'None'
threshold9Display.SelectNormalArray = 'None'
threshold9Display.SelectTangentArray = 'None'
threshold9Display.OSPRayScaleArray = 'Coordinates'
threshold9Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold9Display.SelectOrientationVectors = 'Coordinates'
threshold9Display.ScaleFactor = 0.09987303747406032
threshold9Display.SelectScaleArray = 'Coordinates'
threshold9Display.GlyphType = 'Arrow'
threshold9Display.GlyphTableIndexArray = 'Coordinates'
threshold9Display.GaussianRadius = 0.004993651873703015
threshold9Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold9Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold9Display.OpacityArray = ['POINTS', 'Coordinates']
threshold9Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold9Display.DataAxesGrid = 'GridAxesRepresentation'
threshold9Display.PolarAxes = 'PolarAxesRepresentation'
threshold9Display.ScalarOpacityFunction = coordinatesPWF
threshold9Display.ScalarOpacityUnitDistance = 1.4124180411121245
threshold9Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold9Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold9Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold9Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold9Display.ScaleTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold9Display.OpacityTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# show data from extractSurface2
extractSurface2Display = Show(extractSurface2, renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface2Display.Representation = 'Surface'
extractSurface2Display.ColorArrayName = ['POINTS', 'Coordinates']
extractSurface2Display.LookupTable = coordinatesLUT
extractSurface2Display.Specular = 1.0
extractSurface2Display.SelectTCoordArray = 'None'
extractSurface2Display.SelectNormalArray = 'None'
extractSurface2Display.SelectTangentArray = 'None'
extractSurface2Display.EdgeColor = [0.0, 0.0, 0.0]
extractSurface2Display.OSPRayScaleArray = 'Coordinates'
extractSurface2Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface2Display.SelectOrientationVectors = 'Coordinates'
extractSurface2Display.ScaleFactor = 0.09987303747406032
extractSurface2Display.SelectScaleArray = 'Coordinates'
extractSurface2Display.GlyphType = 'Arrow'
extractSurface2Display.GlyphTableIndexArray = 'Coordinates'
extractSurface2Display.GaussianRadius = 0.004993651873703015
extractSurface2Display.SetScaleArray = ['POINTS', 'Coordinates']
extractSurface2Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface2Display.OpacityArray = ['POINTS', 'Coordinates']
extractSurface2Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface2Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface2Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface2Display.SelectInputVectors = ['POINTS', 'Coordinates']
extractSurface2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface2Display.ScaleTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface2Display.OpacityTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# show data from tube2
tube2Display = Show(tube2, renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
tube2Display.ColorArrayName = ['POINTS', '']
tube2Display.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
tube2Display.Specular = 1.0
tube2Display.SelectTCoordArray = 'None'
tube2Display.SelectNormalArray = 'TubeNormals'
tube2Display.SelectTangentArray = 'None'
tube2Display.EdgeColor = [0.0, 0.0, 0.0]
tube2Display.OSPRayScaleArray = 'Coordinates'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'Coordinates'
tube2Display.ScaleFactor = 0.10109622376039624
tube2Display.SelectScaleArray = 'Coordinates'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'Coordinates'
tube2Display.GaussianRadius = 0.005054811188019813
tube2Display.SetScaleArray = ['POINTS', 'Coordinates']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'Coordinates']
tube2Display.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display.DataAxesGrid = 'GridAxesRepresentation'
tube2Display.PolarAxes = 'PolarAxesRepresentation'
tube2Display.SelectInputVectors = ['POINTS', 'Coordinates']
tube2Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube2Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display.ScaleTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display.OpacityTransferFunction.Points = [-1.386472225189209, 0.0, 0.5, 0.0, 4.080188274383545, 1.0, 0.5, 0.0]

# show data from threshold10
threshold10Display = Show(threshold10, renderView8, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold10Display.Representation = 'Surface'
threshold10Display.AmbientColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
threshold10Display.ColorArrayName = [None, '']
threshold10Display.DiffuseColor = [0.6666666666666666, 0.21176470588235294, 0.19607843137254902]
threshold10Display.Specular = 1.0
threshold10Display.SelectTCoordArray = 'None'
threshold10Display.SelectNormalArray = 'None'
threshold10Display.SelectTangentArray = 'None'
threshold10Display.OSPRayScaleArray = 'Coordinates'
threshold10Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold10Display.SelectOrientationVectors = 'Coordinates'
threshold10Display.ScaleFactor = 0.0999999953674319
threshold10Display.SelectScaleArray = 'Coordinates'
threshold10Display.GlyphType = 'Arrow'
threshold10Display.GlyphTableIndexArray = 'Coordinates'
threshold10Display.GaussianRadius = 0.004999999768371594
threshold10Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold10Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold10Display.OpacityArray = ['POINTS', 'Coordinates']
threshold10Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold10Display.DataAxesGrid = 'GridAxesRepresentation'
threshold10Display.PolarAxes = 'PolarAxesRepresentation'
threshold10Display.ScalarOpacityUnitDistance = 0.7388222152624305
threshold10Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold10Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold10Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold10Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold10Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold10Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# show data from tTKIcospheresFromPoints3
tTKIcospheresFromPoints3Display = Show(tTKIcospheresFromPoints3, renderView8, 'GeometryRepresentation')

# get color transfer function/color map for 'CriticalType'
criticalTypeLUT = GetColorTransferFunction('CriticalType')
criticalTypeLUT.RGBPoints = [0.0, 0.0, 0.129412, 0.584314, 1.5000000000000013, 0.917647, 0.941176, 0.788235, 3.0, 0.0, 0.431373, 0.0]
criticalTypeLUT.ColorSpace = 'RGB'
criticalTypeLUT.AboveRangeColor = [1.0, 1.0, 1.0]
criticalTypeLUT.NanColor = [0.0, 0.0, 0.0]
criticalTypeLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tTKIcospheresFromPoints3Display.Representation = 'Surface'
tTKIcospheresFromPoints3Display.ColorArrayName = ['POINTS', 'CriticalType']
tTKIcospheresFromPoints3Display.LookupTable = criticalTypeLUT
tTKIcospheresFromPoints3Display.Specular = 1.0
tTKIcospheresFromPoints3Display.SelectTCoordArray = 'None'
tTKIcospheresFromPoints3Display.SelectNormalArray = 'Normals'
tTKIcospheresFromPoints3Display.SelectTangentArray = 'None'
tTKIcospheresFromPoints3Display.EdgeColor = [0.0, 0.0, 0.0]
tTKIcospheresFromPoints3Display.OSPRayScaleArray = 'Coordinates'
tTKIcospheresFromPoints3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints3Display.SelectOrientationVectors = 'Coordinates'
tTKIcospheresFromPoints3Display.ScaleFactor = 0.29999999403953553
tTKIcospheresFromPoints3Display.SelectScaleArray = 'Coordinates'
tTKIcospheresFromPoints3Display.GlyphType = 'Arrow'
tTKIcospheresFromPoints3Display.GlyphTableIndexArray = 'Coordinates'
tTKIcospheresFromPoints3Display.GaussianRadius = 0.014999999701976777
tTKIcospheresFromPoints3Display.SetScaleArray = ['POINTS', 'Coordinates']
tTKIcospheresFromPoints3Display.ScaleTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints3Display.OpacityArray = ['POINTS', 'Coordinates']
tTKIcospheresFromPoints3Display.OpacityTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints3Display.DataAxesGrid = 'GridAxesRepresentation'
tTKIcospheresFromPoints3Display.PolarAxes = 'PolarAxesRepresentation'
tTKIcospheresFromPoints3Display.SelectInputVectors = ['POINTS', 'Coordinates']
tTKIcospheresFromPoints3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKIcospheresFromPoints3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIcospheresFromPoints3Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIcospheresFromPoints3Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# show data from extractSurface3
extractSurface3Display = Show(extractSurface3, renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface3Display.Representation = 'Surface'
extractSurface3Display.ColorArrayName = [None, '']
extractSurface3Display.Specular = 1.0
extractSurface3Display.SelectTCoordArray = 'None'
extractSurface3Display.SelectNormalArray = 'None'
extractSurface3Display.SelectTangentArray = 'None'
extractSurface3Display.EdgeColor = [0.0, 0.0, 0.0]
extractSurface3Display.OSPRayScaleArray = 'Coordinates'
extractSurface3Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSurface3Display.SelectOrientationVectors = 'Coordinates'
extractSurface3Display.ScaleFactor = 0.0999999953674319
extractSurface3Display.SelectScaleArray = 'Coordinates'
extractSurface3Display.GlyphType = 'Arrow'
extractSurface3Display.GlyphTableIndexArray = 'Coordinates'
extractSurface3Display.GaussianRadius = 0.004999999768371594
extractSurface3Display.SetScaleArray = ['POINTS', 'Coordinates']
extractSurface3Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSurface3Display.OpacityArray = ['POINTS', 'Coordinates']
extractSurface3Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSurface3Display.DataAxesGrid = 'GridAxesRepresentation'
extractSurface3Display.PolarAxes = 'PolarAxesRepresentation'
extractSurface3Display.SelectInputVectors = ['POINTS', 'Coordinates']
extractSurface3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
extractSurface3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSurface3Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSurface3Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# show data from tube3
tube3Display = Show(tube3, renderView8, 'GeometryRepresentation')

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = [None, '']
tube3Display.Specular = 1.0
tube3Display.SelectTCoordArray = 'None'
tube3Display.SelectNormalArray = 'TubeNormals'
tube3Display.SelectTangentArray = 'None'
tube3Display.EdgeColor = [0.0, 0.0, 0.0]
tube3Display.OSPRayScaleArray = 'Coordinates'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'Coordinates'
tube3Display.ScaleFactor = 0.10148541554808617
tube3Display.SelectScaleArray = 'Coordinates'
tube3Display.GlyphType = 'Arrow'
tube3Display.GlyphTableIndexArray = 'Coordinates'
tube3Display.GaussianRadius = 0.005074270777404308
tube3Display.SetScaleArray = ['POINTS', 'Coordinates']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'Coordinates']
tube3Display.OpacityTransferFunction = 'PiecewiseFunction'
tube3Display.DataAxesGrid = 'GridAxesRepresentation'
tube3Display.PolarAxes = 'PolarAxesRepresentation'
tube3Display.SelectInputVectors = ['POINTS', 'Coordinates']
tube3Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tube3Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube3Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube3Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# show data from threshold11
threshold11Display = Show(threshold11, renderView8, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold11Display.Representation = 'Surface'
threshold11Display.ColorArrayName = [None, '']
threshold11Display.Specular = 1.0
threshold11Display.SelectTCoordArray = 'None'
threshold11Display.SelectNormalArray = 'TubeNormals'
threshold11Display.SelectTangentArray = 'None'
threshold11Display.OSPRayScaleArray = 'Coordinates'
threshold11Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold11Display.SelectOrientationVectors = 'Coordinates'
threshold11Display.ScaleFactor = 0.0999999953674319
threshold11Display.SelectScaleArray = 'Coordinates'
threshold11Display.GlyphType = 'Arrow'
threshold11Display.GlyphTableIndexArray = 'Coordinates'
threshold11Display.GaussianRadius = 0.004999999768371594
threshold11Display.SetScaleArray = ['POINTS', 'Coordinates']
threshold11Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold11Display.OpacityArray = ['POINTS', 'Coordinates']
threshold11Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold11Display.DataAxesGrid = 'GridAxesRepresentation'
threshold11Display.PolarAxes = 'PolarAxesRepresentation'
threshold11Display.ScalarOpacityUnitDistance = 0.2965275639969653
threshold11Display.OpacityArrayName = ['POINTS', 'Coordinates']
threshold11Display.SelectInputVectors = ['POINTS', 'Coordinates']
threshold11Display.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
threshold11Display.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold11Display.ScaleTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold11Display.OpacityTransferFunction.Points = [-1.5449261665344238, 0.0, 0.5, 0.0, 4.47632360458374, 1.0, 0.5, 0.0]

# hide data in view
Hide(tTKScalarFieldNormalizer1, renderView8)

# hide data in view
Hide(threshold9, renderView8)

# hide data in view
Hide(extractSurface2, renderView8)

# hide data in view
Hide(threshold10, renderView8)

# hide data in view
Hide(extractSurface3, renderView8)

# hide data in view
Hide(tube3, renderView8)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView9'
# ----------------------------------------------------------------

# show data from start_data_omega_bzvti
start_data_omega_bzvtiDisplay_7 = Show(start_data_omega_bzvti, renderView9, 'UniformGridRepresentation')

# trace defaults for the display properties.
start_data_omega_bzvtiDisplay_7.Representation = 'Outline'
start_data_omega_bzvtiDisplay_7.AmbientColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_7.ColorArrayName = [None, '']
start_data_omega_bzvtiDisplay_7.DiffuseColor = [0.1803921568627451, 0.17647058823529413, 0.17647058823529413]
start_data_omega_bzvtiDisplay_7.SelectTCoordArray = 'None'
start_data_omega_bzvtiDisplay_7.SelectNormalArray = 'None'
start_data_omega_bzvtiDisplay_7.SelectTangentArray = 'None'
start_data_omega_bzvtiDisplay_7.OSPRayScaleArray = 'bz_wz'
start_data_omega_bzvtiDisplay_7.OSPRayScaleFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_7.SelectOrientationVectors = 'None'
start_data_omega_bzvtiDisplay_7.ScaleFactor = 1.006182531816462
start_data_omega_bzvtiDisplay_7.SelectScaleArray = 'None'
start_data_omega_bzvtiDisplay_7.GlyphType = 'Arrow'
start_data_omega_bzvtiDisplay_7.GlyphTableIndexArray = 'None'
start_data_omega_bzvtiDisplay_7.GaussianRadius = 0.050309126590823094
start_data_omega_bzvtiDisplay_7.SetScaleArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_7.ScaleTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_7.OpacityArray = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_7.OpacityTransferFunction = 'PiecewiseFunction'
start_data_omega_bzvtiDisplay_7.DataAxesGrid = 'GridAxesRepresentation'
start_data_omega_bzvtiDisplay_7.PolarAxes = 'PolarAxesRepresentation'
start_data_omega_bzvtiDisplay_7.ScalarOpacityUnitDistance = 0.12315087617612483
start_data_omega_bzvtiDisplay_7.OpacityArrayName = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_7.SliceFunction = 'Plane'
start_data_omega_bzvtiDisplay_7.Slice = 63
start_data_omega_bzvtiDisplay_7.SelectInputVectors = ['POINTS', 'bz_wz']
start_data_omega_bzvtiDisplay_7.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
start_data_omega_bzvtiDisplay_7.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
start_data_omega_bzvtiDisplay_7.ScaleTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
start_data_omega_bzvtiDisplay_7.OpacityTransferFunction.Points = [-0.7038620845610734, 0.0, 0.5, 0.0, 9.253598515594783, 1.0, 0.5, 0.0]

# show data from contour1
contour1Display_7 = Show(contour1, renderView9, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display_7.Representation = 'Surface'
contour1Display_7.ColorArrayName = ['POINTS', '']
contour1Display_7.Opacity = 0.2
contour1Display_7.Specular = 1.0
contour1Display_7.SelectTCoordArray = 'None'
contour1Display_7.SelectNormalArray = 'Normals'
contour1Display_7.SelectTangentArray = 'None'
contour1Display_7.EdgeColor = [0.0, 0.0, 0.0]
contour1Display_7.OSPRayScaleArray = 'omega_bz'
contour1Display_7.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display_7.SelectOrientationVectors = 'None'
contour1Display_7.ScaleFactor = 0.8636709690093994
contour1Display_7.SelectScaleArray = 'omega_bz'
contour1Display_7.GlyphType = 'Arrow'
contour1Display_7.GlyphTableIndexArray = 'omega_bz'
contour1Display_7.GaussianRadius = 0.04318354845046997
contour1Display_7.SetScaleArray = ['POINTS', 'omega_bz']
contour1Display_7.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display_7.OpacityArray = ['POINTS', 'omega_bz']
contour1Display_7.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display_7.DataAxesGrid = 'GridAxesRepresentation'
contour1Display_7.PolarAxes = 'PolarAxesRepresentation'
contour1Display_7.SelectInputVectors = ['POINTS', 'Normals']
contour1Display_7.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display_7.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display_7.ScaleTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display_7.OpacityTransferFunction.Points = [0.5, 0.0, 0.5, 0.0, 0.5001220703125, 1.0, 0.5, 0.0]

# show data from tTKIcospheresFromPoints2
tTKIcospheresFromPoints2Display_1 = Show(tTKIcospheresFromPoints2, renderView9, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints2Display_1.Representation = 'Surface'
tTKIcospheresFromPoints2Display_1.ColorArrayName = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display_1.LookupTable = cellDimensionLUT
tTKIcospheresFromPoints2Display_1.Specular = 1.0
tTKIcospheresFromPoints2Display_1.SelectTCoordArray = 'None'
tTKIcospheresFromPoints2Display_1.SelectNormalArray = 'Normals'
tTKIcospheresFromPoints2Display_1.SelectTangentArray = 'None'
tTKIcospheresFromPoints2Display_1.EdgeColor = [0.0, 0.0, 0.0]
tTKIcospheresFromPoints2Display_1.OSPRayScaleArray = 'CellDimension'
tTKIcospheresFromPoints2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display_1.SelectOrientationVectors = 'None'
tTKIcospheresFromPoints2Display_1.ScaleFactor = 0.866682767868042
tTKIcospheresFromPoints2Display_1.SelectScaleArray = 'CellDimension'
tTKIcospheresFromPoints2Display_1.GlyphType = 'Arrow'
tTKIcospheresFromPoints2Display_1.GlyphTableIndexArray = 'CellDimension'
tTKIcospheresFromPoints2Display_1.GaussianRadius = 0.043334138393402104
tTKIcospheresFromPoints2Display_1.SetScaleArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display_1.OpacityArray = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
tTKIcospheresFromPoints2Display_1.DataAxesGrid = 'GridAxesRepresentation'
tTKIcospheresFromPoints2Display_1.PolarAxes = 'PolarAxesRepresentation'
tTKIcospheresFromPoints2Display_1.SelectInputVectors = ['POINTS', 'CellDimension']
tTKIcospheresFromPoints2Display_1.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
tTKIcospheresFromPoints2Display_1.OSPRayScaleFunction.Points = [-41.2251014709473, 0.0, 0.5, 0.0, 48.8776016235352, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tTKIcospheresFromPoints2Display_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tTKIcospheresFromPoints2Display_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'omega_bz'
omega_bzPWF = GetOpacityTransferFunction('omega_bz')
omega_bzPWF.Points = [0.4000000059604645, 0.0, 0.5, 0.0, 0.997122049331665, 1.0, 0.5, 0.0]
omega_bzPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CellDimension'
cellDimensionPWF = GetOpacityTransferFunction('CellDimension')
cellDimensionPWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
cellDimensionPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'CriticalType'
criticalTypePWF = GetOpacityTransferFunction('CriticalType')
criticalTypePWF.Points = [0.0, 0.0, 0.5, 0.0, 3.0, 1.0, 0.5, 0.0]
criticalTypePWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(tTKIcospheresFromPoints3)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')