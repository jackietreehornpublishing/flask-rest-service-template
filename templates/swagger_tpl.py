# -*- coding: utf-8 -*-
from apispec import APISpec
from marshmallow import Schema, fields


__all__ = ['spec']


spec = APISpec(
    title='${package_name}',
    version='${version}',
    info=dict(
        description='${description}'
    ),
    plugins=['apispec.ext.marshmallow']
)


#foreach($t in $contract.typeRegistry().allTypes())
class ${t.name()}Schema(Schema):
#foreach($f in $t.fields())
#set ($field_type = $f.contractType().name() )
  #if( $field_type == "Integer")
${f.name()} = fields.Int()
#elseif( $field_type == "String")
${f.name()} = fields.String()
#elseif( $field_type == "Boolean")
${f.name()} = fields.Boolean()
#elseif( $field_type == "Float")
${f.name()} = fields.Float()
#elseif( $field_type == "Date")
${f.name()} = fields.Date()
#elseif( $field_type == "DateTime")
${f.name()} = fields.DateTime()
#end
#end
    
spec.definition('${t.name()}', schema=${t.name()}Schema)
#end


#foreach($op in $contract.ops())
spec.add_path(
    path='/${op.path()}',
    operations=dict(
        get=dict(
            responses={
                '${op.responses().success().code()}': {
                    'schema': {'$ref': '#/definitions/${op.responses().success().contractType().name()}'}
                }
            }
        )
    )
)
#end
