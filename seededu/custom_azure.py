from storages.backends.azure_storage import AzureStorage
from django.conf import settings

class AzureMediaStorage(AzureStorage):
    account_name = 'testseed' # Must be replaced by your <storage_account_name>
    account_key = 'WctSajPO8wuS7PZ6n9MBW8yHoL65jsgdRMVTMe1Z5ijIVsCzIduqHUhM1DG8QdMM+a/1NywQd/qLY4cbTvvnaQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'testseed' # Must be replaced by your storage_account_name
    account_key = 'WctSajPO8wuS7PZ6n9MBW8yHoL65jsgdRMVTMe1Z5ijIVsCzIduqHUhM1DG8QdMM+a/1NywQd/qLY4cbTvvnaQ==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None

# class AzureMediaStorage(AzureStorage):
#     location = 'media'
#     file_overwrite = False


# class AzureStaticStorage(AzureStorage):
#     location = 'static'
#     file_overwrite = False