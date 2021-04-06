import sim
import sys

sim.simxFinish(-1)
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=-1:
    print ('Connected to remote API server')
else:
    print ('Failed connecting to remote API server')
    sys.exit("could not connect!")
while True:
    errorcode, left_motor_handle  = sim.simxGetObjectHandle(clientID, "Pioneer_p3dx_leftMotor", sim.simx_opmode_oneshot_wait)
    errorcode, right_motor_handle = sim.simxGetObjectHandle(clientID, "Pioneer_p3dx_rightMotor", sim.simx_opmode_oneshot_wait)

    errorcode = sim.simxSetJointTargetVelocity(clientID, left_motor_handle, 0.9, sim.simx_opmode_streaming)
    errorcode = sim.simxSetJointTargetVelocity(clientID, right_motor_handle, 0.9, sim.simx_opmode_streaming)

    errorcode, sensor_handle_5 = sim.simxGetObjectHandle(clientID, "Pioneer_p3dx_ultrasonicSensor5", sim.simx_opmode_oneshot_wait)

    returnCode, detectionState, detectedPoint, detectedObjectHandle, detectedSurfaceNormalVector = sim.simxReadProximitySensor(clientID, sensor_handle_5, sim.simx_opmode_oneshot_wait)
    print(f"returncode = {returnCode} /n decectionState = {detectionState} \n detectedPoint = {detectedPoint} \n detectedObjectHandle = {detectedObjectHandle} \n detectedSurfaceNormalVector ={detectedSurfaceNormalVector} ")