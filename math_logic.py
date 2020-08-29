def factoriser(equation):
  terms_init = equation.split('+')
  print(terms_init)
  terms = [term.split('-') for term in terms_init]
  square = str(terms[0][0])
  x = str(terms[1][0])
  constant = str(terms[2][0])
  sign1 = None
  sign2 = None
  if equation.count('+') == 2:
      sign1 = '+'
      sign2 = '+'
  elif equation.count('-') == 2:
      sign1 = '-'
      sign2 = '-'
  elif equation.count('+') == 1:
      if str(terms_init[0]).count('-') == 0:
          sign1 = '+'
          sign2 = '-'
      else:
          sign1 = '-'
          sign2 = '+'
  if len(square) > 3:
    coeffecient_of_square = list(square)[0]
  else:
    coeffecient_of_square = 1
  if len(x) > 1:
    coeffecient_of_x = list(x)[0]
  else:
    coeffecient_of_x = 1
  factor_list = []
  if sign1 == sign2:
      multiplied = int(coeffecient_of_square) * int(constant)
  else:
      multiplied = (int(coeffecient_of_square) * int(constant)) * -1
  for trial_number in range(1, multiplied + 1):
      if multiplied % trial_number == 0:
          factor_list.append(trial_number)
          factor_list.append(trial_number * -1)
      else:
          pass
  middle_term = None
  needed = False
  for number1 in factor_list:
      for number2 in factor_list:
          if (number1 + number2) == int(coeffecient_of_x):
              middle_term = [number1, number2]
              break
          else:
              pass
  if middle_term is None:
      return 'Failed to solve with factorisation. Quadratic formula needs to be used. Kindly do it your self.'
  else:
    string_fin = ''
    if middle_term[0] > 0:
        sign_1 = '+'
    else:
        sign_1 = '-'
    if middle_term[1] > 0:
        sign_2 = '+'
    else:
      sign_2 = '-'
    string_fin += equation + '\n'
    string2 = '=>{0}x^2{1}'
    if coeffecient_of_square != 1:
        string_format0 = coeffecient_of_square
    else:
        string_format0 = ''
    if (abs(middle_term[0]) != 1) and (abs(middle_term[1]) != 1):
        string_format1 = sign_1 + str(abs(middle_term[0])) + 'x' + sign_2 + str(abs(middle_term[1])) + 'x' + sign2 \
                        + constant
    elif (abs(middle_term[0]) == 1) and (abs(middle_term[1]) != 1):
        string_format1 = sign_1 + 'x' + sign_2 + str(abs(middle_term[1])) + 'x' + sign2 + constant
    elif (abs(middle_term[0]) != 1) and (abs(middle_term[1]) == 1):
        string_format1 = sign_1 + str(abs(middle_term[0])) + 'x' + sign_2 + 'x' + sign2 + constant
    else:
        string_format1 = sign_1 + 'x' + sign_2 + 'x' + sign2 + constant
    string_fin += string2.format(string_format0, string_format1 + '\n')
    string3 = '=>{0}x({1}x{2}){3}({4})\n'
    if abs(middle_term[0]) % int(coeffecient_of_square) != 0:
        string_format0 = ''
        string_format1 = coeffecient_of_square
        string_format3_tool = int(coeffecient_of_square)
        string_format2 = sign_1 + str(middle_term[0] / coeffecient_of_square)
    else:
        string_format1 = ''
        string_format3_tool = 1
        string_format2 = sign_1 + str(abs(middle_term[0]))
    if abs(middle_term[1]) % string_format3_tool == 0:
        if abs(middle_term[1]) != 1:
            string_format3 = sign_2 + str(abs(middle_term[1]))
        else:
            string_format3 = sign_2
        string_format4 = 'x' + sign2 + constant
    else:
        string_format3 = sign_2
        string_format4 = str(abs(middle_term[1])) + 'x' + sign2 + constant
    string_fin += string3.format(string_format0, string_format1, string_format2, string_format3, string_format4)
    if string_format3 == sign_2:
        string_format3 += str(abs(middle_term[1]))
    string_fin += 'so, (' + string_format0 + 'x' + string_format3 + ')(' + string_format4 + ')'
    return string_fin
