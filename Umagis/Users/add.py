from Users import models

user = models.Users(name='MIHARIMANANA', user_name='Angelo', genre='Mâle',matricule_number='ETS-3822',
                    classe='EM2', pass_word_hashed='260702',contacte='miharimananaangelo@yahoo.com',
                    image_path='kratos.jpeg')

user.save()

