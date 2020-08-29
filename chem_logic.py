from mendeleev import element
def emprical_formula(elements, amounts):
  rams = []
  for elem in elements:
      rams.append(element(elem).atomic_weight)
  answers = []
  for amount, ram in zip(amounts, rams):
      answer = float(amount) / round(ram)
      answers.append(answer)
  min_answer = answers[0]
  for answer in answers:
      if answer < min_answer:
          min_answer = answer
  answer_set2 = []
  for answer in answers:
      answer2 = answer / min_answer
      answer_set2.append(answer2)
  answer_set2_copy = [answer_i for answer_i in answer_set2]
  m_needed = False
  for answer_2, itering in zip(answer_set2, range(len(answer_set2))):
      if ((answer_2 % 1 != 0) and (answer_2 > round(answer_2)) and (answer_2 - round(answer_2) > 0.1)) or \
              ((answer_2 < round(answer_2)) or(round(answer_2) - answer_2 > 0.1) or (answer_2 % 1 != 0)):
          if (answer_2 * 2) % 1 == 0:
              answer_set2[itering] = answer_2 * 2
              multi = 2
              answer_set2_copy.remove(answer_2)
          elif (answer_2 * 3) % 1 == 0:
              answer_set2[itering] = answer_2 * 2
              multi = 3
              answer_set2_copy.remove(answer_2)
          elif (answer_2 * 4) % 1 == 0:
              answer_set2[itering] = answer_2 * 2
              multi = 4
              answer_set2_copy.remove(answer_2)
          elif (answer_2 * 5) % 1 == 0:
              answer_set2[itering] = answer_2 * 2
              multi = 5
              answer_set2_copy.remove(answer_2)
          else:
              multi = 1
              answer_set2[itering] = round(answer_2)
          for answer_copy,  loop in zip(answer_set2_copy, range(len(answer_set2))):
              answer_copy *= multi
              if loop != itering:
                  answer_set2[loop] = answer_copy
      else:
          answer_set2[itering] = round(answer_2)
  string = ''
  for symbol, number in zip(elements, answer_set2):
      string += symbol
      if number != 1:
          string += str(int(number))
  return 'Empirical formula => ' + string
def formula_mass(formula):
  string = ''
  rfm = 0
  formula1 = formula + '='
  string += formula1
  for char in formula:
    if char.isdigit():
      list_ = formula.split(char)
      list1 = [list_[i] for i in range(1, len(list_))]
      formula = ''.join(list1)
      for index in range(int(char)):
        rfm += int(round(element(list_[0]).atomic_weight))
      string += char + 'x' + str(round(element(list_[0]).atomic_weight)) + '+'
  string = string[:-1]
  string += '\n=' + str(rfm)
  return string
def formula_mass_advanced(items, occurences):
  items = items.split(',')
  occurences = occurences.split(',')
  string = ''
  rfm = 0
  for i, j in zip(items, occurences):
    for k in range(int(j)):
      rfm += int(round(element(i).atomic_weight))
    string += str(j) + 'x' + str(round(element(i).atomic_weight)) + '+'
  string = string[:-1]
  string += '\n=' + str(rfm)
  return string
