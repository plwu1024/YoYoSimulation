# from vpython import *
# import os

# g = 9.8
# T = 50
# yoyo_m = 0.2
# size, size_middle = 0.03, 0.005
# hand_pos = vec(0, 0, 0)
# L = 1
# k = 10000
# Inertia = yoyo_m * size**2 * 0.5
# omega = 0

# scene = canvas(title='yo-yo', background=vec(1, 1, 0.6))
# rope = cylinder(pos =vec(0, 0, 0), radius=0.0005)
# middle_cy = cylinder(radius=size_middle, axis=vec(0.0015, 0 ,0), texture=textures.stucco)
# middle_cy.pos = - 0.5 * middle_cy.axis 
# middle_cy.v = vec(0, 0, 0)

# dt = 0.0001
# while True:
#     rate(10000)
#     rope.axis = middle_cy.pos + 0.5 * middle_cy.axis - hand_pos
#     if rope.axis.mag > L:
#         tension = -k * (rope.axis.mag - L) * rope.axis.norm()
# #        os.system("pause")
#         break
#     else:
#         tension = vec(0, 0, 0)
#     gravity = yoyo_m * g
#     yoyo_a_unsigned = yoyo_m / (yoyo_m + Inertia / size_middle**2)
#     alpha = yoyo_a_unsigned / size_middle
#     omega += alpha * dt
#     middle_cy.rotate(angle=omega*dt, axis=vec(1, 0 ,0))
# #    middle_cy.a = vec(0, -g, 0) + tension / yoyo_m
#     middle_cy.a = vec(0, -yoyo_a_unsigned, 0) + tension / yoyo_m
#     middle_cy.v +=  middle_cy.a * dt
#     middle_cy.pos += middle_cy.v * dt
#     scene.center = middle_cy.pos

# print("alpha =", alpha)
# print('omega =', omega)
# from vpython import *
# import os

# g = 9.8
# m_yoyo = 0.2 #yoyo's total mass
# size_disk, size_axle = 0.03, 0.005
# axle_thickness = 0.002
# disk_thickness = 0.015 #兩側圓盤的厚度
# hand_pos = vec(0, 0, 0) #手的位置
# L, k = 1, 10000 #繩子長度與係數
# Inertia = m_yoyo * size_disk**2 * 0.5 #yoyo's total moment of inertia
# omega = 0 #yoyo's 角速度

# # axle: 輪軸
# # disk: 兩側圓盤
# scene = canvas(title='yo-yo', background=vec(1, 1, 0.6))
# rope = cylinder(pos =vec(0, 0, 0), axis=vec(0, 0, 0), radius=0.0005)
# axle = cylinder(radius=size_axle, axis=vec(axle_thickness, 0 ,0), texture=textures.metal)
# disk_left = cylinder(radius=size_disk, axis=vec(disk_thickness, 0 ,0), texture=textures.wood)
# disk_right = cylinder(radius=size_disk, axis=vec(disk_thickness, 0 ,0), texture=textures.wood)
# axle.pos = - 0.5 * axle.axis
# disk_left.pos = axle.pos - disk_left.axis
# disk_right.pos = -axle.pos
# axle.v = vec(0, 0, 0)
# #disk_left.v = vec(0, 0, 0)
# #disk_right.v = vec(0, 0, 0)

# '''def acceleration_of_Yoyo(m, r, I=Inertia):
#     return m*g / (m + (I/r**2))
# '''
# dt = 0.001
# stage = 1
# while True:
#     rate(300)
#     rope.axis = axle.pos + axle.axis * 0.5 - hand_pos
    
# #繩子尚未放盡-> stage1

#     if stage == 1:
# #        a_unsigned = acceleration_of_Yoyo(m_yoyo, size_axle)
#         a_unsigned = -m_yoyo*g / (m_yoyo + (Inertia/size_axle**2))
#         if rope.axis.mag > L:
#             os.system("pause")
#             stage = 2
# #        tension = -k * (rope.axis.mag - L) * rope.axis.norm()
#         print(a_unsigned)
#         pass
# #        break

# #繩子到最長，懸停空轉-> stage2
#     elif stage == 2:
#         axle.v = vec(0, 0, 0)
#         a_unsigned = 0
#         os.system("pause")
#         stage = 3
# #        tension = -k * (rope.axis.mag - L) * rope.axis.norm()
#         pass 

# #繩子逐漸收回-> stage3
#     elif stage == 3:
#         a_unsigned = m_yoyo*g / (m_yoyo + (Inertia/size_axle**2))
#         if rope.axis.y >= 0:
#             print("axle.a =", axle.a)
#             print("axle.v =", axle.v)
#             os.system("pause")
#             stage = 1
#         pass

# #請檢查程式
#     else :
#         raise ValueError('Unable to identify the current situation of the yoyo')
#         break
#     alpha = a_unsigned / size_axle
#     omega += alpha * dt
#     axle.rotate(angle=omega*dt, axis=vec(1, 0 ,0))
#     disk_left.rotate(angle=omega*dt, axis=vec(1, 0 ,0))
#     disk_right.rotate(angle=omega*dt, axis=vec(1, 0 ,0))
#    #axle.a = vec(0, -g, 0) + tension / m_yoyo
#    #axle.a = vec(0, -a_unsigned, 0) + tension / m_yoyo
#     axle.a = vec(0, a_unsigned, 0) / m_yoyo
#     axle.v +=  axle.a * dt
#     axle.pos += axle.v * dt
#     disk_left.pos = axle.pos - disk_left.axis
#     disk_right.pos = axle.pos + axle.axis
#     scene.center = axle.pos

# print("alpha =", alpha)
# print('omega =', omega)
#from vpython import *
# import os

# g = -9.8
# m_yoyo = 0.2 #yoyo's total mass
# size_disk, size_axle = 0.03, 0.005# axle:輪軸, disk:兩側圓盤
# disk_thickness = 0.015 #兩側圓盤的厚度
# hand_pos = vec(0, 0, 0) #手的位置
# L, k = 1, 10e3 #繩子長度與係數
# Inertia = m_yoyo * size_disk**2 * 0.5 #yoyo's total moment of inertia
# omega = 0 #yoyo的角速度


# scene = canvas(title='yo-yo', background=vec(1, 1, 0.6), height=1200, width=300)
# rope = cylinder(pos =vec(0, 0, 0), axis=vec(0, 0, 0), radius=0.0005)
# axle = cylinder(radius=size_axle, axis=vec(0.002, 0 ,0), texture=textures.metal)
# disk_left = cylinder(radius=size_disk, axis=vec(disk_thickness, 0 ,0), texture=textures.wood)
# disk_right = cylinder(radius=size_disk, axis=vec(disk_thickness, 0 ,0), texture=textures.wood)
# axle.pos = - 0.5 * axle.axis
# axle.v = vec(0, 0, 0)

# T, dt = 0, 0.001
# stage = 1
# while True:
# 	rate(100)
# 	T += dt
# 	rope.axis = axle.pos + axle.axis * 0.5 - hand_pos

# #繩子尚未放盡-> stage1
# 	if stage == 1:
# 		alpha_pseudoscalar = m_yoyo*g / (m_yoyo * size_axle - Inertia)
# 		a_pseudoscalar = alpha_pseudoscalar * size_axle
# 		if rope.axis.mag > L:
# 			stage = 2
# 			continue

# #繩子到最長，懸停空轉-> stage2
# 	elif stage == 2:
# 		alpha_pseudoscalar = 0
# 		tension = k * (rope.axis.mag - L)
# 		a_pseudoscalar = (tension + m_yoyo * g) / m_yoyo
# 		if T>2:
# 			stage = 3
# 			axle.v = vec(0, -omega*size_axle, 0)
# 			continue

# #繩子逐漸收回-> stage3
# 	elif stage == 3:
# 		alpha_pseudoscalar = -m_yoyo*g / (m_yoyo * size_axle - Inertia)
# 		a_pseudoscalar = -alpha_pseudoscalar * size_axle
# 		if axle.v.y <= 0:
# 			stage = 4
# 			continue

# #yoyo在你手中(歸零)
# 	elif stage == 4:
# 		a_pseudoscalar, alpha_pseudoscalar = 0, 0
# 		tension = 0
# 		axle.a, axle.v, axle.pos = vec(0, 0, 0), vec(0, 0, 0), vec(0, 0, 0)
# 		omega = 0
# 		if True:
# 			stage = 1
# 			continue

# #請檢查程式
# 	else :
# 		raise ValueError('Unable to identify the current situation of the yoyo')
# 		break

# #無關stage的部分
# 	omega += alpha_pseudoscalar* dt
# 	axle.rotate(angle=-omega*dt, axis=vec(1, 0 ,0))
# 	disk_left.rotate(angle=-omega*dt, axis=vec(1, 0 ,0))
# 	disk_right.rotate(angle=-omega*dt, axis=vec(1, 0 ,0))
# 	axle.a = vec(0, a_pseudoscalar, 0)
# 	axle.v += axle.a * dt
# 	axle.pos += axle.v * dt
# 	disk_left.pos = axle.pos - disk_left.axis
# 	disk_right.pos = axle.pos + axle.axis
# #	scene.center = (axle.pos + hand_pos)/2
# 	scene.center = axle.pos
from vpython import *
import math
# import os

g = -9.8
m_yoyo = 0.2 #yoyo's total mass
size_disk, size_axle = 0.03, 0.005# axle:輪軸, disk:兩側圓盤
disk_thickness = 0.01 #兩側圓盤的厚度
hand_pos = vec(0, 0, 0) #手的位置
L, k = 1, 10e3 #繩子長度與係數
Inertia = m_yoyo * size_disk**2 * 0.5 #yoyo's total moment of inertia
omega = 0 #yoyo的角速度
disk_num = 50

def keyinput(evt):
	global stage, axle
	s = evt.key
	print(s)
	if s == "up" and stage == 2:
		stage = 3
		axle.v = vec(0, -omega*size_axle, 0)
	elif s == "down" and stage ==4:
		stage = 1

class wood_yoyo_disk(cylinder):
	def __init__(self, *a, **b):
		super().__init__(texture=textures.wood, axis=vec(disk_thickness/disk_num, 0 ,0), *a, **b)

scene = canvas(title='yo-yo', background=vec(1, 1, 0.6), height=800, width=300)
scene.bind('keydown', keyinput)
rope = cylinder(pos =vec(0, 0, 0), axis=vec(0, 0, 0), radius=0.0005)
axle = cylinder(radius=size_axle, axis=vec(0.002, 0 ,0), texture=textures.metal)
# A = 2 * size_disk / disk_thickness
disk_l = [wood_yoyo_disk(radius=size_disk/disk_num*(math.sqrt(30*i) + 1)) for i in range(disk_num)]
disk_r = [wood_yoyo_disk(radius=size_disk/disk_num*(math.sqrt(30*i) + 1)) for i in range(disk_num)]
#disk_right = cylinder(radius=size_disk, axis=vec(disk_thickness, 0 ,0), texture=textures.wood)
axle.pos = - 0.5 * axle.axis
axle.v = vec(0, 0, 0)

alpha = m_yoyo*g / (m_yoyo * size_axle - Inertia)
accel = alpha * size_axle

T, dt = 0, 0.001
stage = 1
while True:
	rate(40)
	T += dt
	rope.axis = axle.pos + axle.axis * 0.5 - hand_pos

	#繩子尚未放盡-> stage1
	if stage == 1:
		omega += alpha* dt
		axle.a = vec(0, accel, 0)
		if rope.axis.mag > L:
			stage = 2
			continue

	#繩子到最長，懸停空轉-> stage2
	elif stage == 2:
		tension = k * (rope.axis.mag - L)
		axle.a = vec(0, 1, 0) * ((tension + m_yoyo * g) / m_yoyo)

	#繩子逐漸收回-> stage3
	elif stage == 3:
		omega -= alpha* dt
		axle.a = vec(0, accel, 0)
		if axle.v.y <= 0:
			stage = 4
			tension = 0
			axle.a, axle.v, axle.pos = vec(0, 0, 0), vec(0, 0, 0), vec(0, 0, 0)
			omega = 0
			continue

	#yoyo在你手中(歸零)
	elif stage == 4:
		pass

	#請檢查程式
	else :
		raise ValueError('Unable to identify the current situation of the yoyo')
		break

	#無關stage的部分
	axle.rotate(angle=-omega*dt, axis=vec(1, 0 ,0))
	#disk_right.rotate(angle=-omega*dt, axis=vec(1, 0 ,0))
	axle.v += axle.a * dt
	axle.pos += axle.v * dt
	for i in range(disk_num):
		disk_l[i].rotate(angle=-omega*dt, axis=vec(1, 0 ,0))
		disk_l[i].pos = axle.pos - disk_l[i].axis - vec(disk_thickness/disk_num*i, 0, 0)
	for i in range(disk_num):
		disk_r[i].rotate(angle=-omega*dt, axis=vec(1, 0 ,0))
		disk_r[i].pos = axle.axis + axle.pos + vec(disk_thickness/disk_num*i, 0, 0)
	#disk_right.pos = axle.pos + axle.axis
	#scene.center = (axle.pos + hand_pos)/2
	scene.center = axle.pos