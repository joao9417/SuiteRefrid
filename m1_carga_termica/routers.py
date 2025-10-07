#routers.py
class CargaTermicaRouter:
    """
    Un router para controlar todas las operaciones de la BD
    para modelos en la aplicacion m1_carga_termica.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'm1_carga_termica':
            return 'm1_carga_termica_db'
        return None
    
    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'm1_carga_termica':
            return 'm1_carga_termica_db'
        return None
    
    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'm1_carga_termica' or\
              obj2._meta.app_label == 'm1_carga_termica':
                return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
         if app_label == 'm1_carga_termica':
              return db == 'm1_carga_termica_db'
         return None