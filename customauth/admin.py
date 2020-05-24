from django.contrib import admin

# Register your models here.
from .models import (
    Application,
    AuthToken,
)



admin.site.register(
    [
    
        Application,
        AuthToken,
        
    ]
)