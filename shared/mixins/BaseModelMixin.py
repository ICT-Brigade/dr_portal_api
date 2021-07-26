from shared import models


class BaseModelMixin(models.BaseModel, models.BaseTimestampedModel):
	class Meta:
		abstract = True
