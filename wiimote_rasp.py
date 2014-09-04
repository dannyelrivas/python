import cwiid, time

button_delay = 0.1

print 'Presionar botones 1 y 2 para sincronizar Wiimote...'
time.sleep(1)

# en estas lineas se crea la coneccion con el wiimote, si no se ocnecta se cierra
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "No hay coneccion wiimote"
  quit()

print 'Wiimote conectado!\n'
print 'presionar botones para prbar coneccion\n'
print 'Boton (+) y (-) cierran coneccion.\n'

time.sleep(3)

wii.rpt_mode = cwiid.RPT_BTN

while True:

  buttons = wii.state['botones']

  # si (+) y (-) se precionan cierra el programa
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\ncerrando coneccion ...'
  
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)

  # aqui se detectan botones precionados y se imprimen en pantalla
  if (buttons & cwiid.BTN_LEFT):
    print '← IZQ'
    time.sleep(button_delay)

  if(buttons & cwiid.BTN_RIGHT):
    print '→ DER'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_UP):
    print '↑ ARRIBA '
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_DOWN):
    print '↓ ABAJO '
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_1):
    print '- 1 -'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_2):
    print '- 2 -'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_A):
    print '- A -'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_B):
    print '- B -'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_HOME):
    wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC
    check = 0
    while check == 0:
      print(wii.state['acc'])
      time.sleep(0.01)
      check = (buttons & cwiid.BTN_HOME)
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_MINUS):
    print 'Boton (-)'
    time.sleep(button_delay)

  if (buttons & cwiid.BTN_PLUS):
    print 'Boton (+)'
    time.sleep(button_delay)
