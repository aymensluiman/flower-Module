<?xml version="1.0" encoding="utf-8" ?>
<openerp>
  <data>
     <!--    Flower WorkFlow -->
     <record id="flower_workflow_id" model="workflow">
      <field name="name">Flower Purchase Workflow</field>
      <field name="osv">request.data</field>
      <field name="on_create">True</field>
     
     </record>
     <!--    Flower  Activity -->
    <record id="draft_activity_id"  model="workflow.activity">
      <field name="wkf_id"   ref="flower_workflow_id"/>
      <field name="flow_start">True</field>
      <field name="name">draft</field>
      <field name="kind">function</field>
      <field name="action">write({'state' : 'draft'})</field>
    </record>
    <record id="confirmed_activity_id"  model="workflow.activity">
      <field name="wkf_id"   ref="flower_workflow_id"/>
      
      <field name="name">confirm</field>
      <field name="kind">function</field>
      <field name="action">write({'state' : 'confirmed'})</field>
    </record>
    <record id="approve_activity_id" model="workflow.activity">
      <field name="wkf_id"   ref="flower_workflow_id"/>
      <field name="name">approve</field>
      <field name="kind">function</field>
      <field name="action">write({'state' : 'approved'})</field>
    </record>
    <record id="done_actitvity_id"  model="workflow.activity">
      <field name="wkf_id"   ref="flower_workflow_id"/>
      <field name="name">done</field>
      <field name="kind">function</field>
      <field name="action">done()</field>
      <field name="flow_stop">True</field> 
    </record>
    <record id="cancel_activity_id"  model="workflow.activity">
      <field name="wkf_id"    ref="flower_workflow_id"/>
      <field name="name">cancel</field>
      <field name="kind">function</field>
      <field name="action">write({'state':'cancel'})</field>
      <field name="flow_stop">True</field>
    </record>
<!--      Flower WorkFlow Transition   -->
    <record id="draft_confirm_tran_id"   model="workflow.transition">
      <field name="act_from"    ref="draft_activity_id"/>
      <field name="act_to"   ref="confirmed_activity_id"/>
      <field name="signal">confirm</field>
    </record>
    <record id="confirm_approve_tran_id"   model="workflow.transition">
      <field name="act_from"    ref="confirmed_activity_id"/>
      <field name="act_to"   ref="approve_activity_id"/>
      <field name="signal">approve</field>
    </record>
     <record id="approve_done_tran_id"   model="workflow.transition">
      <field name="act_from"    ref="approve_activity_id"/>
      <field name="act_to"   ref="done_actitvity_id"/>
      <field name="signal">done</field>
    </record>
    <record id="confirm_cancel_tran_id"   model="workflow.transition">
      <field name="act_from"    ref="confirmed_activity_id"/>
      <field name="act_to"   ref="cancel_activity_id"/>
      <field name="signal">cancel</field>
    </record>
    <record id="approve_cancel_tran_id"   model="workflow.transition">
      <field name="act_from"    ref="approve_activity_id"/>
      <field name="act_to"   ref="cancel_activity_id"/>
      <field name="signal">cancel</field>
    </record>








































  </data>
</openerp>
