#-----------------------------------------------------------
# Test Custom Function for ORS Dragonfly    
# Using Python 3.6                          
#                                           
# Created By:   Michael T. Kuczynski        
# Created On:   05/10/2018                  
# Version:      1.0   
# Details:      Affine transformation function                      
#-----------------------------------------------------------

from ORSModel import Channel
from ORSModel import ROI, MultiROI, orsVect, orsColor
channel = Channel()
channel.setTitle('demo channel')
#set it sizes, since we use the default voxel size, the channel is for now 100 meter cube
channel.setXYZTSize(100,100,100,1)
channel.setXSpacing(0.01)
channel.setYSpacing(0.01)
channel.setZSpacing(0.01)
#now the channel is 1 meter cube
#initilize it for float32 data
channel.initializeDataForFLOAT()
channelBox = channel.getBox()
channelBox.grow(orsVect(-channelBox.getDirection0Size()*0.5, -channelBox.getDirection1Size()*0.5, -channelBox.getDirection2Size()*0.5))
channel.paintBox(channelBox,  1, 0)
channel.setDataDirty()
#publish it so that it is visible in the Object properties list
channel.publish()

roiA = ROI()
roiA.setTitle('roiA')
roiA.copyShapeFromStructuredGrid(channel)
roiA.setInitialColor(orsColor(1,0,0,1))
roiA.paintSphere(roiA.getBox().getOrigin(), roiA.getBox().getDirection0Size(), 1, 0)
roiA.publish()

multiROIa= MultiROI()
multiROIa.setTitle('multiROIa')
multiROIa.copyShapeFromStructuredGrid(roiA)
multiROIBox = multiROIa.getBox()
multiROIa.setLabelCount(3)
multiROIBox.grow(orsVect(-multiROIBox.getDirection0Size()*0.5, -multiROIBox.getDirection1Size()*0.5, -multiROIBox.getDirection2Size()*0.5))
multiROIBox.setOrigin(multiROIa.getOrigin())
multiROIa.paintBox(multiROIBox,  1, 0)

multiROIBox.setOrigin(multiROIa.getBox().getCenter())
multiROIa.paintBox(multiROIBox,  2, 0)

multiROIBox.setOrigin((multiROIa.getBox().getOriginOpposite() - multiROIa.getBox().getOrigin())*0.25)
multiROIa.paintBox(multiROIBox,  3, 0)
multiROIa.publish()