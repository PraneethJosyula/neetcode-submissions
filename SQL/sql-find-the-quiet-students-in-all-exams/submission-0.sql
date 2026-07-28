-- Write your query below
with exam_stats as(
  select exam_id, max(score) as maxs, min(score) as mins
  from exam
  group by exam_id
),
loud as(
  select distinct s.student_id
  from exam s join exam_stats e on s.exam_id = e.exam_id
  where s.score = e.maxs or s.score = e.mins 
)

select st.student_id, st.student_name from
student st
where st.student_id not in (select * from loud) and st.student_id in (select student_id from exam)
order by st.student_id;