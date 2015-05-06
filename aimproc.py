import mechanize

br = mechanize.Browser()
br.open("http://www.aim.env.uea.ac.uk/aim/model4/model4d.php")
br.form = list(br.forms())[0]

output_mode = br.form.find_control("wwwOutputMode")
br[output_mode.name]=["column"]


input_area = br.form.find_control("tf")
input_area.value = "298.15 1.0 1.0  1 0  0.42  3. 1. 0.  1. 2. 0. 0. 0. 0.  3 3 4 3 3  0 \r\n 273.15 1.0 1.0  1 0  0.42  3. 1. 0.  1. 2. 0. 0. 0. 0.  3 3 4 3 3  0"

response = br.submit()

response = response.read()

parts = response.split('--\n\n')

out1header = parts[1].split('\n')[0]
out1content = parts[1].split('\n\n\n\n')[0].split('\n')[1:]

out2header = parts[2].split('\n')[0]
out2content = parts[2].split('\n\n\n\n')[0].split('\n')[1:]

out3header = parts[3].split('\n')[0]
out3content = parts[3].split('\n </pre')[0].split('\n')[1:]




