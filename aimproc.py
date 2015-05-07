import mechanize

br = mechanize.Browser()
br.open("http://www.aim.env.uea.ac.uk/aim/model4/model4d.php")
br.form = list(br.forms())[0]

output_mode = br.form.find_control("wwwOutputMode")
br[output_mode.name]=["column"]

#AIM batch input as:
# T(K) pressure(keep as 1atm) volume(keep as 1m3)  water_flag(use 1 for fixed RH) water_dissociation_flag(default 0) H+ NH4+ Na+ SO42- NO3- Cl- Br- OH- NH3 HNO3_partition flag(3 = suppress, 4= suppress but report pHNO3) HCl_partition_flag NH3_partition_flag H2SO4_partition_flag HBr_partition_flag(must be 3) solid_formation_flag(0 = allow all solids)

data_in = "298.15 1.0 1.0  1 0  0.42  3. 1. 0.  1. 2. 0. 0. 0. 0.  3 3 4 3 3  0 \r\n 273.15 1.0 1.0  1 0  0.42  3. 1. 0.  1. 2. 0. 0. 0. 0.  3 3 4 3 3  0\r\n 273.15 1.0 1.0  1 0  0.42  3. 1. 0.  1. 2. 0. 0. 0. 0.  3 3 4 3 3  0\r\n 273.15 1.0 1.0  1 0  0.42  3. 1. 0.  1. 2. 0. 0. 0. 0.  3 3 4 3 3  0\r\n 273.15 1.0 1.0  1 0  0.42  3. 1. 0.  1. 2. 0. 0. 0. 0.  3 3 4 3 3  0\r\n 273.15 1.0 1.0  1 0  0.42  3. 1. 0.  1. 2. 0. 0. 0. 0.  3 3 4 3 3  0"


input_area = br.form.find_control("tf")
input_area.value = data_in

response = br.submit()

response = response.read()

parts = response.split('--\n\n')

out1header = parts[1].split('\n')[0].split()
out1content = parts[1].split('\n\n\n\n')[0].split('\n')[1:]
out1content = [content.split() for content in out1content]
out1content = [[float(i) for i in row] for row in out1content]

out2header = parts[2].split('\n')[0].split()
out2content = parts[2].split('\n\n\n\n')[0].split('\n')[1:]
out2content = [content.split() for content in out2content]
out2content = [[float(i) for i in row] for row in out2content]

out3header = parts[3].split('\n')[0].split()
out3content = parts[3].split('\n </pre')[0].split('\n')[1:]
out3content = [content.split() for content in out3content]
out3content = [[float(i) for i in row] for row in out3content]



