with mart_gh_stargazer as (
    select *
    from {{ source('mart', 'mart_gh_stargazer') }}
),
mart_gh_cumulative as (
    select *
    from {{ ref('mart_gh_cumulative') }}
),

select 
    mart_gh_stargazer.repository
from mart_gh_stargazer
left join mart_gh_cumulative on mart_gh_stargazer.repository = mart_gh_cumulative.repository
