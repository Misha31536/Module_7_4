# Использование %:
team1_num = 5
print('В команде Мастера кода участников: %s' % (team1_num), '!')
team2_num = 6
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num), '!')
# Использование format():
score_2 = 42
print('Команда Волшебники данных решила задач: {}'.format(score_2), '!')
team1_time = 1552.512
print('Волшебники данных решили задачи за {}'.format(team1_time), 'c !')
# Использование f-строк:
score_1 = 40
print(f'Команды решили {score_1} и {score_2} задач.')
challenge_result = 'Мастера кода'
print(f'Результат битвы: победа команды {challenge_result}!')
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = team2_time + team1_time
print(time_avg)
print(f'"Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg / tasks_total:.2f} секунды на задачу!.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    print('Победа команды Мастера кода!')
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    print(f'Победа команды Волшебники Данных!')
else:
    print('Ничья')