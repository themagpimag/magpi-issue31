#!/usr/bin/python
import math
import sys
import argparse

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('-a', '--altitude')
   parser.add_argument('-p', '--pressure')
   parser.add_argument('-m', '--msl')
   args = parser.parse_args()
   if args.altitude is None:
      args.altitude = 112.2  # Value from my GPS for my house
   if args.pressure is None:
      print "Pressure value required"
      sys.exit(40)
   if args.msl is None:
      args.msl = 1013.25
   args.pressure = float(args.pressure)
   args.altitude = float(args.altitude)
   args.msl = float(args.msl)

   print "Alt:", args.altitude, "Pressure:", args.pressure, "MSL:", args.msl
   print "Sealevel:",args.pressure/pow(1-(args.altitude/44330.0),5.255)
   print "Alt:",(44330.0*(1-pow(args.pressure/args.msl,1/5.255)))

