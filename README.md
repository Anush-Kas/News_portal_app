# News_portal_app

```python
py manage.py shell    
from newsportal.models import *
u1 = User.objects.create_user(username='Anton')
u2 = User.objects.create_user(username='Marina')
Author.objects.create(authorUser=u1)
Author.objects.create(authorUser=u2)
Category.objects.create(name='Sport')
Category.objects.create(name='Culture')
Category.objects.create(name='IT')
Category.objects.create(name='Tourism')
Category.objects.create(name='Incidents')
author = Author.objects.get(id=1)
author1 = Author.objects.get(id=2)
Post.objects.create(author = author, categoryType='AR', title='МОК пересмотрел результаты Олимпийских игр-1900', text='Междунаро
дный олимпийский комитет (МОК) пересмотрел результаты Олимпийских игр-1900 в Париже. Об этом сообщил директор МОК по коммуникациям М
арк Адамс, слова которого приводит ТАСС. Исполком передал передал Франции медаль Великобритании, которую завоевал Ллойд Гильдебранд 
в велогонке на 25 километров на треке.')

Post.objects.create(author = author, categoryType='AR', title='МОК пересмотрел результаты Олимпийских игр-1900', text='Междунаро
дный олимпийский комитет (МОК) пересмотрел результаты Олимпийских игр-1900 в Париже. Об этом сообщил директор МОК по коммуникациям М
арк Адамс, слова которого приводит ТАСС. Исполком передал передал Франции медаль Великобритании, которую завоевал Ллойд Гильдебранд 
в велогонке на 25 километров на треке. «Недавние исследования привели к выводу, что, несмотря на тот факт, что Гильдебранд был гражд
анином Великобритании, он родился и вырос во Франции и выступал за французский клуб до и после Игр в Париже 1900 года», — объяснил А
дамс. Французы выиграли медальный зачет Олимпиады-1900 — на счету команды теперь 27 золотых, 39 серебряных и 37 бронзовых наград. У 
Великобритании 31 награда (15-7-9) и третье место в зачете. Олимпийские игры-2024 пройдут в Париже с 26 июля по 11 августа 2024 года.')

Post.objects.create(author = author, categoryType='AR', title='Москвичам покажут моноспектакль о путешествии по жизни от первого
 лица', text='Московский «Электротеатр Станиславский» представляет премьеру моноспектакля российского актера театра и кино Александр
а Синюкова. Премьера состоится во вторник, 18 июня, в 20:00, рассказали «Ленте.ру» в культурном учреждении. По словам организаторов,
 моноспектакль является путешествием по жизни в 16 эпизодах, рассказанным, показанным и спетым самим героем. «Из песен, авторских ри
сунков и искренних рассказов из прошлого и настоящего складывается простой и трогательный спектакль про доверие между людьми и про ценность частного опыта как чего-то очень важного», — говорится в пресс-релизе.')

Post.objects.get(id=3).text
Post.objects.create(author = author1, categoryType='NW', title='В Шебекино после обрушения дома повреждены 20 квартир', text='БЕ
ЛГОРОД, 14 июн - РИА Новости. Около 20 квартир повреждены после частичного обрушения дома в белгородском Шебекино, сообщил губернато
р Белгородской области Вячеслав Гладков. Подъезд многоквартирного дома обрушился в Шебекино после обстрела ВСУ. По последним данным, пострадали семь человек.')

Post.objects.get(id=4).text
Post.objects.create(author = author1, categoryType='AR', title='ИИ помог предотвратить 95 процентов врачебных ошибок', text='По 
словам доктора медицинских наук Карена С. Нанджи, довольно часто врачи допускают ошибки при выборе и назначении лекарственных препар
атов во время операции. По словам ученого, модели ИИ способны анализировать действия врачей и предотвращать огромное количество ошиб
ок. В ходе исследования специалисты изучили отчеты о безопасности, связанные с ошибками в приеме лекарств, задокументированные врача
ми-анестезиологами при хирургических процедурах с августа 2020 года по август 2022-го. Два независимых рецензента классифицировали к
аждую ошибку по времени и типу. В итоге медики выявили 80 ошибок при приеме лекарств и обнаружили, что 76 из них — или 95 процентов 
от общего числа — можно было избежать. Нанджи и его коллеги посоветовали внедрять и использовать ИИ-модели, которые бы контролировал
и действия врачей и подстраховывали медиков. «Хотя поддержка принятия клинических решений повышает эффективность и качество медицинской помощи в операционных, она все еще находится на ранних стадиях внедрения», — заявила соавтор исследования Линда Амичи.')

Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=2))
Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
Post.objects.get(id=4).postCategory.add(Category.objects.get(id=5))
Post.objects.get(id=5).postCategory.add(Category.objects.get(id=3))
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='Очень интересная статья)')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='Очень рад за Францию и Великобританию)')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='Как прекрасно)')
u3= User.objects.create_user(username='Nikita')
Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=u3, text='Как прекрасно)') 
u4= User.objects.create_user(username='Kiril')
Comment.objects.get(id=1).like()
Comment.objects.get(id=1).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=2).like()
Comment.objects.get(id=3).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=4).like()
Comment.objects.get(id=1).dislike()
Comment.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).like()
Post.objects.get(id=2).dislike()
Post.objects.get(id=2).dislike()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).like()
Post.objects.get(id=3).dislike()
Post.objects.get(id=3).dislike()
Post.objects.get(id=3).dislike()
Post.objects.get(id=4).dislike()
Post.objects.get(id=4).dislike()
Post.objects.get(id=4).dislike()
Post.objects.get(id=4).dislike()
Post.objects.get(id=4).dislike()
Post.objects.get(id=4).like()
Post.objects.get(id=4).like()
Post.objects.get(id=4).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).like()
Post.objects.get(id=5).dislike()
Post.objects.get(id=5).dislike()
Comment.objects.create(commentPost=Post.objects.get(id=5), commentUser=u4, text='Это не бот)')
Comment.objects.create(commentPost=Post.objects.get(id=5), commentUser=u4, text='Я не уверен, что это работает так хорошо, как пишут)')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=u3, text='Как прекрасно')
Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=u3, text='пу-пу-пу')
Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=u4, text='пу-пу-пу, заварю-ка кофейку')
Comment.objects.create(commentPost=Post.objects.get(id=4), commentUser=u3, text='как правильно тут все')
Comment.objects.get(id=10).dislike()
Comment.objects.get(id=10).dislike()
Comment.objects.get(id=10).dislike()
Comment.objects.get(id=10).dislike()
Comment.objects.get(id=10).dislike()
Comment.objects.get(id=10).dislike()
Comment.objects.get(id=10).like()
Comment.objects.get(id=10).like()
Comment.objects.get(id=10).like()
Comment.objects.get(id=10).like()
Comment.objects.get(id=9).like()
Comment.objects.get(id=9).like()
Comment.objects.get(id=9).like()
Comment.objects.get(id=8).like()
Comment.objects.get(id=8).like()
Comment.objects.get(id=8).like()
Comment.objects.get(id=8).like()
Comment.objects.get(id=8).like()
Comment.objects.get(id=8).like()
Comment.objects.get(id=8).dislike()
Comment.objects.get(id=7).dislike()
Comment.objects.get(id=7).like()
Comment.objects.get(id=7).like()
Comment.objects.get(id=7).like()
Comment.objects.get(id=7).like()
Comment.objects.get(id=7).like()
Comment.objects.get(id=7).like()
Comment.objects.get(id=6).like()
Comment.objects.get(id=6).like()
Comment.objects.get(id=6).like()
Comment.objects.get(id=6).like()
Comment.objects.get(id=6).like()
Comment.objects.get(id=6).dislike()
Comment.objects.get(id=6).dislike()
Comment.objects.get(id=6).dislike()
Comment.objects.get(id=6).dislike()
Comment.objects.get(id=6).dislike()
Comment.objects.get(id=6).dislike()
Comment.objects.get(id=5).dislike()
Comment.objects.get(id=5).dislike()
Comment.objects.get(id=5).dislike()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).like()
Comment.objects.get(id=5).rating
a = Author.objects.get(id=1)
a.update_rating()
a.ratingAuthor
b = Author.objects.get(id=2)
b.update_rating()
b.ratingAuthor


