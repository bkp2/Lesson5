# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

# TODO здесь ваш код
import room_1 as r1
import room_2 as r2
print('В комнате room1 живут', ', '.join(r1.folks))
print('В комнате room2 живут', ', '.join(r2.folks))

