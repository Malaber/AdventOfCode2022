script_number = ARGV[0]

day_input_file = "inputs/#{script_number}.txt"
day_code_file = "days/#{script_number}.rb"

exit 1 if File.exists?(day_input_file)
exit 1 if File.exists?(day_code_file)

File.open(day_input_file, "w"){|f| f.write("")}
File.open(day_code_file, "w"){|f| f.write(
"require_relative '../helpers/input'
lines = get_lines $PROGRAM_NAME
")}
File.open(".gitlab-ci.yml", "a"){|f| f.puts("
day_#{script_number}:
  <<: *ruby_template
")}
