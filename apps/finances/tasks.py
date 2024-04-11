# import os
# from django.conf import settings
# import random
# from celery import shared_task
# from zipfile import ZipFile
# from PIL import Image


# @shared_task
# def make_thumbnails(file_path, thumbnails=[]):
#     os.chdir(settings.IMAGES_DIR)
#     path, file = os.path.split(file_path)
#     file_name, ext = os.path.splitext(file)

#     zip_file = f"{file_name}.zip"
#     results = {'archive_path': f"{settings.MEDIA_URL}images/{zip_file}"}
#     try:
#         img = Image.open(file_path)
#         zipper = ZipFile(zip_file, 'w')
#         zipper.write(file)
#         os.remove(file_path)
#         for w, h in thumbnails:
#             img_copy = img.copy()
#             img_copy.thumbnail((w, h))
#             thumbnail_file = f'{file_name}_{w}x{h}.{ext}'
#             img_copy.save(thumbnail_file)
#             zipper.write(thumbnail_file)
#             os.remove(thumbnail_file)

#         img.close()
#         zipper.close()
#     except IOError as e:
#         print(e)

#     return results



# # @shared_task(name="add")
# # def add(x, y):
# #     # Celery recognizes this as the `movies.tasks.add` task
# #     # the name is purposefully omitted here.
# #     total = x + (y * random.randint(3, 100))
# #     return total

# @shared_task(name="multiply_two_numbers")
# def mul(x, y):
#     # Celery recognizes this as the `multiple_two_numbers` task
#     total = x * (y * random.randint(3, 100))
#     return total

# @shared_task(name="sum_list_numbers")
# def xsum(numbers):
#     # Celery recognizes this as the `sum_list_numbers` task
#     return sum(numbers)
