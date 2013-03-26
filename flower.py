from osv import osv,fields
import time





class supplier_supplier(osv.osv):
      _name = 'supplier.supplier'
      _description = 'suppliers Info'
      _columns = {
               'name' : fields.char('Name',size=32),
               'address' : fields.char('Address',size=32),
               
           }
supplier_supplier()

class flower_flower(osv.osv):
      _name = 'flower.flower'
      _description = 'Flowers info'
      _columns =  {
               'name' : fields.char('Name',size=16,required=True),
               'type' : fields.selection([('Aster','Aster'),('Bird of Paradise','Bird of Paradise'), ('Calla Lily','Calla Lily'),('Carnation','Carnation'),('Daffodil','Daffodil'),('Iris','Iris'),('Cymbidium Orchid','Cymbidium Orchid'),('8',' '),],'Type',),
               'color' : fields.selection([('red','Red'),('white','White'),('orange','Orange'),('pink','Pink'),('violet','Violet'),],'Color',required=True),
               'date' : fields.date('Date'),
               'year' : fields.char('Year' , size=16),
               'supplier_ids' : fields.many2many('supplier.supplier','flo_sup_rel','flowers_id','supplier_id','Suppliers'),
             
         }
flower_flower()





class request_data(osv.osv):
      
      _name = 'request.data'
      _describtion = "Flower Purchase Request"
      _columns = {
             'req_ref' : fields.char('Reference',required=True,readonly=True,size=16),
             
             'cust_name' : fields.char('Customer Name',size=32,required=True ,),
             'time'     : fields.date('Date'),
             'flowers_ids' : fields.one2many('request.request','fl_req_id','Items'),
             'qoute_no' : fields.char('Qoutation No',size=16,readonly=True),
             'state' : fields.selection([('draft','Draft'),('confirmed','confirmed by Manager'),('approved','Approved By Department Manager'),('done','Done'),('cancel','Cancelled'),],'State',readonly=True),
              
                  
                  }
      
      _defaults = {
              'req_ref' : lambda self,cr,uid,ctx : self.pool.get('ir.sequence').get(cr , uid , 'request.data'),
              'state' : 'draft',
                   }
      
      def done(self,cr,uid,ids,context=None):
          
          data = self.browse(cr,uid,ids,context=context)
          for i in data:
              new_id = self.pool.get('qoute').create(cr,uid,{
                                                           
                                                             'cust_name' : i.cust_name,
                                                             'ref' : i.req_ref,
                                                             'date_request' : i.time, 
                                                             'request_id' : ids[0]
                                       
                                    })
              
          print "IDS Number : ",ids     
#           records = self.pool.get('qoute').read(cr,uid,new_id,[],context=context)
#           for record in records:
#               print "Cust Name :",record['cust_name']
#               qoute_no = o.no
#               self.write(cr,uid,ids,{'qoute_no' : qoute_no})
# #              for j in obj:
#                   print "Quantity : ",j.qo
#           for i in data:
#               obj = i.flowers_ids
#               for j in obj:
#                   print "Quantity : ",j.qo
#                   num = j.qo
#                   m = 1
#                   for m in range(num):
#                       new_id = self.pool.get('qoute').create(cr,uid,{
#                                                           
#                          'cust_name' : i.cust_name,
#                          'ref' : i.req_ref,
#                          'date_request' : i.time, 
#                          
#                                       
#                                    })
#                       print "Iteration number : ",m
               
          self.write(cr,uid,ids,{'state' : 'done'})
          return True
     
      def Print_qoute(self,cr,uid,ids,context=None):
          print "Hello Now You are in Function Print_Qoute"
          data = self.pool.get('qoute').browse(cr,uid,5,context=context) 
           
           
          for i in data:
#             if i.request_id == ids :
#                print "Customer Name :", i.cust_name
#             else :
               print "Customer :",i.cust_name    
          return True
      
      
request_data()




class request_request(osv.osv):
      _name = 'request.request'
      
      _columns = {
             'flower_id' : fields.many2one('flower.flower','Items',required=True),
             'fl_req_id':fields.many2one('request.data','Item'),
             'qo': fields.integer('Quantity',required=True),
             'price' : fields.float('Price'),
             'note' : fields.text('Note'),     
             }
      
      
      _sql_constraints = [
           ('flower_id_unique','unique(flower_id)','Some Items is Duplicated....!') 
        ]
      
      _defaults = {
              'price' : 1.0,
              'qo' : 1,
               
                 }
      
      
      
      
                     
request_request()

class qoute(osv.osv):
      _name = 'qoute'
      _columns = {
            'no' : fields.char('No',size=16,readonly=True),
            'cust_name' : fields.char('Customer Name',size=32,readonly=True),
            'ref' : fields.char('References',size=16,readonly=True),
            'date_request' : fields.char('Date Of Request',readonly=True,size=32),
            'date_qoute' : fields.date('Date'),
            'flower_items' : fields.one2many('flower.qoute','ref_qoute','Flowers'),
            'tax' : fields.selection([('15','%15'),('10','%10'),('1',''),],'Tax'),
            'length' : fields.integer('Length Days'),
            'state' : fields.selection([('draft','Draft'),('confirm','Confirm'),('done','Done'),],'State',readonly=True),
            'request_id' : fields.char('Request',size=32)
            
                 
                  }
      
      _defaults = {
           'no' : lambda self,cr,uid,ctx : self.pool.get('ir.sequence').get(cr , uid , 'qoute'),

           'tax' : '1',
           'length' : 0,
           'state' : 'draft',        
                   
                   }
qoute()

                  
class flower_qoute(osv.osv):
      _name = 'flower.qoute'
      _columns = {
          'ref_qoute' : fields.many2one('qoute','Qoutation'),
          'flower_name' : fields.char('Name',size=32),
          'quantity' : fields.integer('Quantity'),
          'supplier' : fields.many2one('supplier.supplier','Supplier'),
          
                  
                  
                  
                  }
      
flower_qoute()from osv import osv,fields
import time





class supplier_supplier(osv.osv):
      _name = 'supplier.supplier'
      _description = 'suppliers Info'
      _columns = {
               'name' : fields.char('Name',size=32),
               'address' : fields.char('Address',size=32),
               
           }
supplier_supplier()

class flower_flower(osv.osv):
      _name = 'flower.flower'
      _description = 'Flowers info'
      _columns =  {
               'name' : fields.char('Name',size=16,required=True),
               'type' : fields.selection([('Aster','Aster'),('Bird of Paradise','Bird of Paradise'), ('Calla Lily','Calla Lily'),('Carnation','Carnation'),('Daffodil','Daffodil'),('Iris','Iris'),('Cymbidium Orchid','Cymbidium Orchid'),('8',' '),],'Type',),
               'color' : fields.selection([('red','Red'),('white','White'),('orange','Orange'),('pink','Pink'),('violet','Violet'),],'Color',required=True),
               'date' : fields.date('Date'),
               'year' : fields.char('Year' , size=16),
               'supplier_ids' : fields.many2many('supplier.supplier','flo_sup_rel','flowers_id','supplier_id','Suppliers'),
             
         }
flower_flower()





class request_data(osv.osv):
      
      _name = 'request.data'
      _describtion = "Flower Purchase Request"
      _columns = {
             'req_ref' : fields.char('Reference',required=True,readonly=True,size=16),
             
             'cust_name' : fields.char('Customer Name',size=32,required=True ,),
             'time'     : fields.date('Date'),
             'flowers_ids' : fields.one2many('request.request','fl_req_id','Items'),
             'qoute_no' : fields.char('Qoutation No',size=16,readonly=True),
             'state' : fields.selection([('draft','Draft'),('confirmed','confirmed by Manager'),('approved','Approved By Department Manager'),('done','Done'),('cancel','Cancelled'),],'State',readonly=True),
              
                  
                  }
      
      _defaults = {
              'req_ref' : lambda self,cr,uid,ctx : self.pool.get('ir.sequence').get(cr , uid , 'request.data'),
              'state' : 'draft',
                   }
      
      def done(self,cr,uid,ids,context=None):
          
          data = self.browse(cr,uid,ids,context=context)
          for i in data:
              new_id = self.pool.get('qoute').create(cr,uid,{
                                                           
                                                             'cust_name' : i.cust_name,
                                                             'ref' : i.req_ref,
                                                             'date_request' : i.time, 
                                                             'request_id' : ids[0]
                                       
                                    })
              
          print "IDS Number : ",ids     
#           records = self.pool.get('qoute').read(cr,uid,new_id,[],context=context)
#           for record in records:
#               print "Cust Name :",record['cust_name']
#               qoute_no = o.no
#               self.write(cr,uid,ids,{'qoute_no' : qoute_no})
# #              for j in obj:
#                   print "Quantity : ",j.qo
#           for i in data:
#               obj = i.flowers_ids
#               for j in obj:
#                   print "Quantity : ",j.qo
#                   num = j.qo
#                   m = 1
#                   for m in range(num):
#                       new_id = self.pool.get('qoute').create(cr,uid,{
#                                                           
#                          'cust_name' : i.cust_name,
#                          'ref' : i.req_ref,
#                          'date_request' : i.time, 
#                          
#                                       
#                                    })
#                       print "Iteration number : ",m
               
          self.write(cr,uid,ids,{'state' : 'done'})
          return True
     
      def Print_qoute(self,cr,uid,ids,context=None):
          print "Hello Now You are in Function Print_Qoute"
          data = self.pool.get('qoute').browse(cr,uid,5,context=context) 
           
           
          for i in data:
#             if i.request_id == ids :
#                print "Customer Name :", i.cust_name
#             else :
               print "Customer :",i.cust_name    
          return True
      
      
request_data()




class request_request(osv.osv):
      _name = 'request.request'
      
      _columns = {
             'flower_id' : fields.many2one('flower.flower','Items',required=True),
             'fl_req_id':fields.many2one('request.data','Item'),
             'qo': fields.integer('Quantity',required=True),
             'price' : fields.float('Price'),
             'note' : fields.text('Note'),     
             }
      
      
      _sql_constraints = [
           ('flower_id_unique','unique(flower_id)','Some Items is Duplicated....!') 
        ]
      
      _defaults = {
              'price' : 1.0,
              'qo' : 1,
               
                 }
      
      
      
      
                     
request_request()

class qoute(osv.osv):
      _name = 'qoute'
      _columns = {
            'no' : fields.char('No',size=16,readonly=True),
            'cust_name' : fields.char('Customer Name',size=32,readonly=True),
            'ref' : fields.char('References',size=16,readonly=True),
            'date_request' : fields.char('Date Of Request',readonly=True,size=32),
            'date_qoute' : fields.date('Date'),
            'flower_items' : fields.one2many('flower.qoute','ref_qoute','Flowers'),
            'tax' : fields.selection([('15','%15'),('10','%10'),('1',''),],'Tax'),
            'length' : fields.integer('Length Days'),
            'state' : fields.selection([('draft','Draft'),('confirm','Confirm'),('done','Done'),],'State',readonly=True),
            'request_id' : fields.char('Request',size=32)
            
                 
                  }
      
      _defaults = {
           'no' : lambda self,cr,uid,ctx : self.pool.get('ir.sequence').get(cr , uid , 'qoute'),

           'tax' : '1',
           'length' : 0,
           'state' : 'draft',        
                   
                   }
qoute()

                  
class flower_qoute(osv.osv):
      _name = 'flower.qoute'
      _columns = {
          'ref_qoute' : fields.many2one('qoute','Qoutation'),
          'flower_name' : fields.char('Name',size=32),
          'quantity' : fields.integer('Quantity'),
          'supplier' : fields.many2one('supplier.supplier','Supplier'),
          
                  
                  
                  
                  }
      
flower_qoute()
