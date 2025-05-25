#!/usr/bin/env python3

from models import Company, Dev, Freebie, session

# Clear existing data
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()

# Add new data
c1 = Company(name="Meta", founding_year=2004)
d1 = Dev(name="Bob")
session.add_all([c1, d1])
session.commit()

c1.give_freebie(d1, "Sticker", 5)
session.commit()
