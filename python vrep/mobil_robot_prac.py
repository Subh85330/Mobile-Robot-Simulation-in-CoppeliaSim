import sim
import sys
import time

sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)
if clientID != -1:
    print('Connected to remote API server')
else:
    print('Failed connecting to remote API server')
    sys.exit("could not connect!")

errorcode, left_joint_handle = sim.simxGetObjectHandle(clientID, "Left_joint", sim.simx_opmode_oneshot_wait)
errorcode, right_joint_handle = sim.simxGetObjectHandle(clientID, "Right_joint", sim.simx_opmode_oneshot_wait)
errorcode, proximaty_sensor_handle = sim.simxGetObjectHandle(clientID, "Proximity_sensor", sim.simx_opmode_oneshot_wait)



def setTargetVelocity(clientID, handle1, handle2, target_vel1, target_vel2, Operation_mode):
    sim.simxSetJointTargetVelocity(clientID, handle1, target_vel1, Operation_mode)
    sim.simxSetJointTargetVelocity(clientID, handle2, target_vel2, Operation_mode)



while True:
    setTargetVelocity(clientID, left_joint_handle, right_joint_handle, 1, 1, sim.simx_opmode_oneshot_wait)


    returnCode, state, detectedPoint, detectedObjhandel, detectedSurfaceNormalVector = sim.simxReadProximitySensor(
        clientID, proximaty_sensor_handle, sim.simx_opmode_streaming)

    print(state)
    if state == True:
        sim.simxSetJointTargetVelocity(clientID, left_joint_handle, -0.8, sim.simx_opmode_oneshot_wait)
        sim.simxSetJointTargetVelocity(clientID, right_joint_handle, -1.2, sim.simx_opmode_oneshot_wait)
        time.sleep(3)

    time.sleep(0.1)
