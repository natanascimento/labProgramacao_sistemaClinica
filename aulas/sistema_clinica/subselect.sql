/*antigo*/
select d.*, to_timestamp (d.clock)::timestamp without time zone as data,
	
	/*unidade*/
	case when strpos (lower(d.name),'far') > 0 then 100
		 when strpos (lower(d.name),'far mini') > 0 then 101
		 when strpos (lower(d.name),'cen') > 0 then 102
		 when strpos (lower(d.name),'med') > 0 then 103
		 when strpos (lower(d.name),'labc') > 0 then 104
		 when strpos (lower(d.name),'hcir') > 0 then 105
		 when strpos (lower(d.name),'fits') > 0 then 106
		 when strpos (lower(d.name),'fits mini') > 0 then 107
		 when strpos (lower(d.name),'ben') > 0 then 108
		 when strpos (lower(d.name),'ita') > 0 then 109
		 when strpos (lower(d.name),'ita mini') > 0 then 110
		 when strpos (lower(d.name),'pro') > 0 then 111
		 when strpos (lower(d.name),'est') > 0 then 112
		 when strpos (lower(d.name),'umb') > 0 then 113
		 when strpos (lower(d.name),'neo') > 0 then 114
		 when strpos (lower(d.name),'nsg') > 0 then 115
		 when strpos (lower(d.name),'nss') > 0 then 116
		 when strpos (lower(d.name),'car') > 0 then 117
		 when strpos (lower(d.name),'cax') > 0 then 118
		 when strpos (lower(d.name),'col') > 0 then 119
		 when strpos (lower(d.name),'gar') > 0 then 120
		 when strpos (lower(d.name),'gir') > 0 then 121
		 when strpos (lower(d.name),'pet') > 0 then 122
		 when strpos (lower(d.name),'pied') > 0 then 123
		 when strpos (lower(d.name),'ara') > 0 then 124
		 when strpos (lower(d.name),'tob') > 0 then 125
		 when strpos (lower(d.name),'vdc') > 0 then 126
		 when strpos (lower(d.name),'fslf') > 0 then 127
		 when strpos (lower(d.name),'espa') > 0 then 128
		 when strpos (lower(d.name),'alg') > 0 then 129
		 when strpos (lower(d.name),'fst') > 0 then 130
		 when strpos (lower(d.name),'pov') > 0 then 131
		 when strpos (lower(d.name),'lag') > 0 then 132
		 when strpos (lower(d.name),'mos') > 0 then 133
		 when strpos (lower(d.name),'sal') > 0 then 134
		 when strpos (lower(d.name),'pa') > 0 then 135
		 when strpos (lower(d.name),'ver') > 0 then 136 
		 when strpos (lower(d.name), 'nin') > 0 then 137 end as id_unidade,

    
    /*estado do ativo*/

    case when strpos (lower(d.value), '1') > 0 then 'down'
         when strpos (lower(d.value), '0') > 0 then 'up' end as estado_ativo

    case when strpos (lower())
		 
from events d
	
where (strpos(lower(d.name), 'ap')) > 0


/*exemplo1*/
with tabela_temp as ( select cod_curso, nom_curso from  cursos )
  select t.cod_curso, t.nom_curso
     from tabela_temp t

/*exemplo2*/
select t.cod_curso, t.nom_curso 
  from ( select cod_curso, nom_curso from cursos ) t

/*alteração_geral*/
select d.*, to_timestamp (d.clock)::timestamp without time zone as data
  from ( 	/*unidade*/
	case when strpos (lower(d.name),'far') > 0 then 100
		 when strpos (lower(d.name),'far mini') > 0 then 101
		 when strpos (lower(d.name),'cen') > 0 then 102
		 when strpos (lower(d.name),'med') > 0 then 103
		 when strpos (lower(d.name),'labc') > 0 then 104
		 when strpos (lower(d.name),'hcir') > 0 then 105
		 when strpos (lower(d.name),'fits') > 0 then 106
		 when strpos (lower(d.name),'fits mini') > 0 then 107
		 when strpos (lower(d.name),'ben') > 0 then 108
		 when strpos (lower(d.name),'ita') > 0 then 109
		 when strpos (lower(d.name),'ita mini') > 0 then 110
		 when strpos (lower(d.name),'pro') > 0 then 111
		 when strpos (lower(d.name),'est') > 0 then 112
		 when strpos (lower(d.name),'umb') > 0 then 113
		 when strpos (lower(d.name),'neo') > 0 then 114
		 when strpos (lower(d.name),'nsg') > 0 then 115
		 when strpos (lower(d.name),'nss') > 0 then 116
		 when strpos (lower(d.name),'car') > 0 then 117
		 when strpos (lower(d.name),'cax') > 0 then 118
		 when strpos (lower(d.name),'col') > 0 then 119
		 when strpos (lower(d.name),'gar') > 0 then 120
		 when strpos (lower(d.name),'gir') > 0 then 121
		 when strpos (lower(d.name),'pet') > 0 then 122
		 when strpos (lower(d.name),'pied') > 0 then 123
		 when strpos (lower(d.name),'ara') > 0 then 124
		 when strpos (lower(d.name),'tob') > 0 then 125
		 when strpos (lower(d.name),'vdc') > 0 then 126
		 when strpos (lower(d.name),'fslf') > 0 then 127
		 when strpos (lower(d.name),'espa') > 0 then 128
		 when strpos (lower(d.name),'alg') > 0 then 129
		 when strpos (lower(d.name),'fst') > 0 then 130
		 when strpos (lower(d.name),'pov') > 0 then 131
		 when strpos (lower(d.name),'lag') > 0 then 132
		 when strpos (lower(d.name),'mos') > 0 then 133
		 when strpos (lower(d.name),'sal') > 0 then 134
		 when strpos (lower(d.name),'pa') > 0 then 135
		 when strpos (lower(d.name),'ver') > 0 then 136 
		 when strpos (lower(d.name), 'nin') > 0 then 137 end as id_unidade,

    
    /*estado do ativo*/

    case when strpos (lower(d.value), '1') > 0 then 'down'
         when strpos (lower(d.value), '0') > 0 then 'up' end as estado_ativo

    case when strpos (lower())
		 
from events d
	
where (strpos(lower(d.name), 'ap')) > 0 ) t
  