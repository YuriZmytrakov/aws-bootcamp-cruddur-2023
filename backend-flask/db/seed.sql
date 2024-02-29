-- this file was manually created
INSERT INTO public.users (display_name, handle, email, cognito_user_id)
VALUES
  ('Andrew Brown', 'andrewbrown' ,'test@gmail.com', '316b95c0-1051-7000-33ab-5783ff804e2c'),
  ('Andrew Bayko', 'bayko' , 'test2@gmail.com', '316b95c0-1051-7000-33ab-5783ff804e2c'),
  ('Londo Mollari', 'londo' , 'lmollari@centari.com', '316b95c0-1051-7000-33ab-5783ff804e2c');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'andrewbrown' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )