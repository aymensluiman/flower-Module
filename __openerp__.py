{
'name':'Flower Module',
'author':'Aymen Sluiman',
'category':'purchasing and Managment',
'description':'Managment to Purchasing Flowers',
'depends':['base'],
'version':'1.0',
'data' : ['sequence/flower_request_sequence.xml',
          'sequence/flower_qoute_sequence.xml',
          'security/security.xml'],
'update_xml':['flower_view.xml',
              'flower_workflow.xml',
              'flower.xml',
              ],
'installable':True,

}
