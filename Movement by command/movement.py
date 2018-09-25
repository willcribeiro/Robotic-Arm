"""<control the arm Lynxmotion by comand.>
    Copyright (C) 2018  WIlliam Ribeiro

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    contact :   https://github.com/willcribeiro or
                 william-cribeiro@bct.ect.ufrn.br
"""


from ufrn_al5d import RoboticArmAL5D
import time
import keyboard

#DEF BASE
base = 0
#LIMITS
min_base = 500
max_base = 2400

#DEF SHOULDER
SHL = 1
#LIMITS
min_SHL = 1200
max_SHL = 2000

#DEF ELBOW
ELB = 2
#LIMITS
min_ELB = 1100
max_ELB = 2000

#DEF WRIST
WRI = 3
#LIMITS
min_WRI = 500
max_WRI = 2500

#DEF GRIPPER
GRI = 4
#LIMITS
min_GRI = 1300
max_GRI = 2400

#PROPRIEDADES DO BRACO: SERVOS E LIMITES DE OPERACAO

properties = [base, min_base, max_base,
              SHL, min_SHL, max_SHL,
              ELB, min_ELB, max_ELB,
              WRI, min_WRI, max_WRI,
              GRI, min_GRI, max_GRI]

home = '#0P1500#1P1500#2P1500#3P1500#4P1500T1500'
arm = RoboticArmAL5D(properties)
arm.setup()

eixo0 = 1500
eixo1 = 1500
eixo2 = 1500
eixo3 = 1500
eixo4 = 1500

if(arm.abre_porta() == -1):
    print ('Erro abrindo a porta serial /dev/ttyS0\nAbortando o programa...\n')
else: 
    print('PROGRAMA  INICIADO\n\n');
    print ('Porta serial /dev/ttyS0 aberta com sucesso\n')
    try:
        arm.envia_comando(home)
        print(' envio para Home: %s \n' % (home))
    except:
         print('Problema no envio do comando\nAbortando o programa...')
   ''' while True:
        if keyboard.is_pressed('a'):
            print('entrei1')
            time.sleep(0.3)
        else:
            print('entrei2')
            time.sleep(0.3)'''
    while True:

        X = input("Insert the comand\n")
        if (X == 'H'):
            try:
                arm.envia_comando(home)
                print(' Send for the position : %s \n' % (home))
            except: 
                print('Erro\nKill de program...')
        #Incremento da base
        elif (X == 'Q'):
            teta = input("Insert the valor\n")
            P = (P/0.09) + 500
            try:
                eixo0 =  P             

                Mov = '#0P%s#1P%s#2P%s#3P%s#4P%sT1500' % (eixo0,eixo1,eixo2,eixo3,eixo4)
                arm.envia_comando(Mov)
                print(' Send for the position : %s \n' % (Mov))
            except:
                print('Erro\nKill de program...')
         #Incremento da SHOULDER
        elif (X == 'W' or X =='S'):
            P = input("Insert the valor\n")
            try:
                if (X == 'W'):
                    eixo1 = eixo1 + P
                else:
                    eixo1 = eixo1 - P

                Mov = '#0P%s#1P%s#2P%s#3P%s#4P%sT1500' % (eixo0,eixo1,eixo2,eixo3,eixo4)
                arm.envia_comando(Mov)
                print(' Send for the position : %s \n' % (Mov))
            except:
                print('Erro\nKill de program...')
        #Incremento da ELBOW
        elif (X == 'Q' or X == 'E'):
            P = input("Insert the valor\n")
            try:
                if (X == 'Q'):
                    eixo2 = eixo2 + P
                else:
                    eixo2 = eixo2 - P

                Mov = '#0P%s#1P%s#2P%s#3P%s#4P%sT1500' % (eixo0,eixo1,eixo2,eixo3,eixo4)
                arm.envia_comando(Mov)
                print(' Send for the position : %s \n' % (Mov))
            except:
                print('Erro\nKill de program...')
        #Incremento da WRIST
        elif (X == 'Z' or X == 'C'):
            P = input("Insert the valor\n")
            try:
                if (X == 'Z'):
                    eixo3 = eixo3 + P
                else:
                    eixo3 = eixo3 - P

                Mov = '#0P%s#1P%s#2P%s#3P%s#4P%sT1500' % (eixo0,eixo1,eixo2,eixo3,eixo4)
                arm.envia_comando(Mov)
                print(' Send for the position : %s \n' % (Mov))
            except:
                print('Erro\nKill de program...')
         #Incremento da GRIPPERT
        elif (X == 'R' or X == 'F'):
            P = input("Insert the valor\n")
            try:
                if (X == 'R'):
                    eixo4 = eixo4 + P
                else:
                    eixo4 = eixo4 - P

                Mov = '#0P%s#1P%s#2P%s#3P%s#4P%sT1500' % (eixo0,eixo1,eixo2,eixo3,eixo4)
                arm.envia_comando(Mov)
                print(' Send for the position : %s \n' % (Mov))
            except:
                print('Erro\nKill de program...')     
  
    arm.fecha_porta()
    print('\nPROGRAMA DEMONSTRACAO FINALIZADO\n\n')
