from sqlalchemy.exc import IntegrityError

from .router import router
from .schemas import ContactForm
from src.models import Contact


@router.post('/contact')
async def contact(form: ContactForm):
    async with Contact.async_session() as session:
        session.add(Contact(**form.dict()))
        try:
            await session.commit()
        except IntegrityError:
            pass
    return {'detail': 'Success'}
