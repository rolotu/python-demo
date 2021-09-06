bri = set(['brazil', 'russia', 'india'])

if 'india' in bri:
  print('india in bri')

if 'usa' in bri:
  print('usa in bri')

bric = bri.copy()
bric.add('china')

if bric.issuperset(bri):
  print('bric is superset bri')

bri.remove('russia')

print(bri & bric)