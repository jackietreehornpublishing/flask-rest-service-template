# -*- coding: utf-8 -*-
__all__ = [#foreach($t in $contract.typeRegistry().allTypes())'${t.name()}'#if( $foreach.hasNext ), #end#end]


#foreach($t in $contract.typeRegistry().allTypes())
class ${t.name()}(object):
    def __init__(self, #foreach($f in $t.fields())${f.name()}=None#if( $foreach.hasNext ), #end#end):
  #foreach($f in $t.fields())
      # ${f.description()}
      self.${f.name()} = ${f.name()}

  #end

   
    # let's pretend for now we serialize to dict
    def to_dict(self):
        return dict(#foreach($f in $t.fields())${f.name()}=self.${f.name()}#if( $foreach.hasNext ), #end#end)


    def from_dict(self, data):
  #foreach($f in $t.fields())
      self.${f.name()} = data.get('${f.name()}')
  #end
        

#end
