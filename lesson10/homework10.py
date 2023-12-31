#     в файлі library написати функцію, котра приймає два числа та показник степеня - теж число. назва функції та
#     аннотація мають бути такими, щоб докстрінга взагалі не була потрібна (что бажає - читаємо Чистий код)
#     функція перемножує два числа, їх добуток підносить до степеня та повертає значення
#     два числа, які перемножаються, можуть бути тільки позиційними аргументами
#     показник степеня може бути тільки іменованим аргументом


#     закешувати результат роботи функції (декоратор cache). подивитися, як вплинув декоратор на роботу mypy та на
#     обмеження на іменованих та порядкових аргументів


#     імпортувати написану функцію в файл main, і там її позапускати з виведенням логів у консоль (print)
#     flake8 mypy pytest та запис всіх залежностей в файл requirements.txt - всі встановлення та послідуючий запис в
#     файл мають виконуватися однією командою make setup


#     написати тести для цієї функції. тести мають в тому числі включати перевірку на помилки типу TypeError anv
#     ValueError... додатково зверніть увагу, що має бути наступний тест: при аргументах -2 (мінус два), 3, та показнику
#     степеня 2, результат має бути 36 (позитивне значення при парному степеню). перевірте також типи отримуваних
#     значень
#     організуйте запуск ВСЬОГО коду однією командою make run. я, як викладач, просто завантажу вашу роботу
#     (3 файла пітона, залежності та мейкфайл) в робочий проект (з існуючим у мене віртуальним оточенням), запущу дану
#     команду і отримаю результат роботи в терміналі. без цього перевірка безпосередньо коду навіть не буде проводитися
#     - відразу на перездачу (як в автошколі - завалив теорію, за руль не пускають)
#     зауважу, що в мейкфайлі у вас має бути лише дві команди на запуск. DRY