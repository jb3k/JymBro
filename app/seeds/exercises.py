from app.models import db, Exercise
import requests


def seed_exercise():

    exercises = [
        {
            "name": "Incline Hammer Curls",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "dumbbell",
            "difficulty": "beginner",
            "workout_id": 1,
            "instructions": "Seat yourself on an incline bench with a dumbbell in each hand. You should pressed firmly against he back with your feet together. Allow the dumbbells to hang straight down at your side, holding them with a neutral grip. This will be your starting position. Initiate the movement by flexing at the elbow, attempting to keep the upper arm stationary. Continue to the top of the movement and pause, then slowly return to the start position."
        },
        {
            "name": "Wide-grip barbell curl",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "barbell",
            "difficulty": "beginner",
            "workout_id": 1,
            "instructions": "Stand up with your torso upright while holding a barbell at the wide outer handle. The palm of your hands should be facing forward. The elbows should be close to the torso. This will be your starting position. While holding the upper arms stationary, curl the weights forward while contracting the biceps as you breathe out. Tip: Only the forearms should move. Continue the movement until your biceps are fully contracted and the bar is at shoulder level. Hold the contracted position for a second and squeeze the biceps hard. Slowly begin to bring the bar back to starting position as your breathe in. Repeat for the recommended amount of repetitions.  Variations:  You can also perform this movement using an E-Z bar or E-Z attachment hooked to a low pulley. This variation seems to really provide a good contraction at the top of the movement. You may also use the closer grip for variety purposes."
        },
        {
            "name": "EZ-bar spider curl",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "barbell",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Start out by setting the bar on the part of the preacher bench that you would normally sit on. Make sure to align the barbell properly so that it is balanced and will not fall off. Move to the front side of the preacher bench (the part where the arms usually lay) and position yourself to lay at a 45 degree slant with your torso and stomach pressed against the front side of the preacher bench. Make sure that your feet (especially the toes) are well positioned on the floor and place your upper arms on top of the pad located on the inside part of the preacher bench. Use your arms to grab the barbell with a supinated grip (palms facing up) at about shoulder width apart or slightly closer from each other. Slowly begin to lift the barbell upwards and exhale. Hold the contracted position for a second as you squeeze the biceps. Slowly begin to bring the barbell back to the starting position as your breathe in. . Repeat for the recommended amount of repetitions.  Variation: You can also use dumbbells when performing this exercise. Just make sure you place the dumbbells on the part of the preacher bench where you would normally sit properly."
        },
        {
            "name": "Hammer Curls",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "dumbbell",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Stand up with your torso upright and a dumbbell on each hand being held at arms length. The elbows should be close to the torso. The palms of the hands should be facing your torso. This will be your starting position. Now, while holding your upper arm stationary, exhale and curl the weight forward while contracting the biceps. Continue to raise the weight until the biceps are fully contracted and the dumbbell is at shoulder level. Hold the contracted position for a brief moment as you squeeze the biceps. Tip: Focus on keeping the elbow stationary and only moving your forearm. After the brief pause, inhale and slowly begin the lower the dumbbells back down to the starting position. Repeat for the recommended amount of repetitions.  Variations: There are many possible variations for this movement. For instance, you can perform the exercise sitting down on a bench with or without back support and you can also perform it by alternating arms; first lift the right arm for one repetition, then the left, then the right, etc."
        },
        {
            "name": "EZ-Bar Curl",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "e-z_curl_bar",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Stand up straight while holding an EZ curl bar at the wide outer handle. The palms of your hands should be facing forward and slightly tilted inward due to the shape of the bar. Keep your elbows close to your torso. This will be your starting position. Now, while keeping your upper arms stationary, exhale and curl the weights forward while contracting the biceps. Focus on only moving your forearms. Continue to raise the weight until your biceps are fully contracted and the bar is at shoulder level. Hold the top contracted position for a moment and squeeze the biceps. Then inhale and slowly lower the bar back to the starting position. Repeat for the recommended amount of repetitions.  Variations: You can also perform this movement using an E-Z attachment hooked to a low pulley. This variation seems to really provide a good contraction at the top of the movement. You may also use the closer grip for variety purposes."
        },
        {
            "name": "Zottman Curl",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "None",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Stand up with your torso upright and a dumbbell in each hand being held at arms length. The elbows should be close to the torso. Make sure the palms of the hands are facing each other. This will be your starting position. While holding the upper arm stationary, curl the weights while contracting the biceps as you breathe out. Only the forearms should move. Your wrist should rotate so that you have a supinated (palms up) grip. Continue the movement until your biceps are fully contracted and the dumbbells are at shoulder level. Hold the contracted position for a second as you squeeze the biceps. Now during the contracted position, rotate your wrist until you now have a pronated (palms facing down) grip with the thumb at a higher position than the pinky. Slowly begin to bring the dumbbells back down using the pronated grip. As the dumbbells close your thighs, start rotating the wrist so that you go back to a neutral (palms facing your body) grip. Repeat for the recommended amount of repetitions."
        },
        {
            "name": "Biceps curl to shoulder press",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "dumbbell",
            "difficulty": "beginner",
            "workout_id": 1,
            "instructions": "Begin in a standing position with a dumbbell in each hand. Your arms should be hanging at your sides with your palms facing forward. Look directly ahead, keeping your chest up, with your feet shoulder-width apart. This will be your starting position. Initiate the movement by flexing the elbows to curl the weight. Do not use momentum or flex through the shoulder, instead use a controlled motion. Execute the pressing movement by extending the arm, flexing and abducting the shoulder to rotate the arm as you press above your head. Pause at the top of the motion before reversing the movement to return to the starting position. Complete the desired number of repetitions before switching to the opposite side."
        },
        {
            "name": "Barbell Curl",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "barbell",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Stand up with your torso upright while holding a barbell at a shoulder-width grip. The palm of your hands should be facing forward and the elbows should be close to the torso. This will be your starting position. While holding the upper arms stationary, curl the weights forward while contracting the biceps as you breathe out. Tip: Only the forearms should move. Continue the movement until your biceps are fully contracted and the bar is at shoulder level. Hold the contracted position for a second and squeeze the biceps hard. Slowly begin to bring the bar back to starting position as your breathe in. Repeat for the recommended amount of repetitions.  Variations:  You can also perform this movement using a straight bar attachment hooked to a low pulley. This variation seems to really provide a good contraction at the top of the movement. You may also use the closer grip for variety purposes."
        },
        {
            "name": "Concentration curl",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "dumbbell",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Sit down on a flat bench with one dumbbell in front of you between your legs. Your legs should be spread with your knees bent and feet on the floor. Use your right arm to pick the dumbbell up. Place the back of your right upper arm on the top of your inner right thigh. Rotate the palm of your hand until it is facing forward away from your thigh. Tip: Your arm should be extended and the dumbbell should be above the floor. This will be your starting position. While holding the upper arm stationary, curl the weights forward while contracting the biceps as you breathe out. Only the forearms should move. Continue the movement until your biceps are fully contracted and the dumbbells are at shoulder level. Tip: At the top of the movement make sure that the little finger of your arm is higher than your thumb. This guarantees a good contraction. Hold the contracted position for a second as you squeeze the biceps. Slowly begin to bring the dumbbells back to starting position as your breathe in. Caution: Avoid swinging motions at any time. Repeat for the recommended amount of repetitions. Then repeat the movement with the left arm.  Variations: This exercise can be performed standing with the torso bent forward and the arm in front of you. In this case, no leg support is used for the back of your arm so you will need to make extra effort to ensure no movement of the upper arm. This is a more challenging version of the exercise and is not recommended for people with lower back issues."
        },
        {
            "name": "Flexor Incline Dumbbell Curls",
            "type": "strength",
            "muscle": "biceps",
            "equipment": "dumbbell",
            "difficulty": "beginner",
            "workout_id": 1,
            "instructions": "Hold the dumbbell towards the side farther from you so that you have more weight on the side closest to you. (This can be done for a good effect on all bicep dumbbell exercises). Now do a normal incline dumbbell curl, but keep your wrists as far back as possible so as to neutralize any stress that is placed on them. Sit on an incline bench that is angled at 45-degrees while holding a dumbbell on each hand. Let your arms hang down on your sides, with the elbows in, and turn the palms of your hands forward with the thumbs pointing away from the body. Tip: You will keep this hand position throughout the movement as there should not be any twisting of the hands as they come up. This will be your starting position. Curl up the two dumbbells at the same time until your biceps are fully contracted and exhale. Tip: Do not swing the arms or use momentum. Keep a controlled motion at all times. Hold the contracted position for a second at the top. As you inhale, slowly go back to the starting position. Repeat for the recommended amount of repetitions.  Caution: Do not extend your arms totally as you could injure your elbows if you hyperextend them. Also, make sure that on the way down you move slowly to avoid injury. Variations: You can use cables for this movement as well."
        },
        {
            "name": "Landmine twist",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "other",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Position a bar into a landmine or securely anchor it in a corner. Load the bar to an appropriate weight. Raise the bar from the floor, taking it to shoulder height with both hands with your arms extended in front of you. Adopt a wide stance. This will be your starting position. Perform the movement by rotating the trunk and hips as you swing the weight all the way down to one side. Keep your arms extended throughout the exercise. Reverse the motion to swing the weight all the way to the opposite side. Continue alternating the movement until the set is complete."
        },
        {
            "name": "Elbow plank",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Get into a prone position on the floor, supporting your weight on your toes and your forearms. Your arms are bent and directly below the shoulder. Keep your body straight at all times, and hold this position as long as possible. To increase difficulty, an arm or leg can be raised."
        },
        {
            "name": "Bottoms Up",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Begin by lying on your back on the ground. Your legs should be straight and your arms at your side. This will be your starting position. To perform the movement, tuck the knees toward your chest by flexing the hips and knees. Following this, extend your legs directly above you so that they are perpendicular to the ground. Rotate and elevate your pelvis to raise your glutes from the floor. After a brief pause, return to the starting position."
        },
        {
            "name": "Suspended ab fall-out",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "other",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Adjust the straps so the handles are at an appropriate height, below waist level. Begin standing and grasping the handles. Lean into the straps, moving to an incline push-up position. This will be your starting position. Keeping your arms straight, lean further into the suspension straps, bringing your body closer to the ground, allowing your shoulders to extend, raising your arms up and over your head. Maintain a neutral spine and keep the rest of your body straight, your shoulders being the only joints allowed to move. Pause during the peak contraction, and then return to the starting position."
        },
        {
            "name": "Dumbbell V-Sit Cross Jab",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "dumbbell",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Begin seated on your butt with your knees bent and feet on the ground. Lean your upper body back to form a 45-degree angle with the floor. Bring your feet off the ground so that your body resembles a \"V\" shape. Grasp a dumbbell in each hand and hold tight to your chest with palms facing each other. This will be your starting position. While keeping your core tight and maintaining your body's \"V\" position, quickly extend your left arm straight out (similar to a jab) and then bring it back to the starting position while simultaneously punching out with the right arm. Your torso and legs may slightly rotate side to side opposite of your hands throughout the movementâ€”this is okay. A punch with each hand counts as one total repetition. Repeat for recommended number of repetitions."
        },
        {
            "name": "Standing cable low-to-high twist",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "cable",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Connect a standard handle on a tower, and move the cable to the lowest pulley position. With your side to the cable, grab the handle with one hand and step away from the tower. You should be approximately armâ€™s length away from the pulley, with the tension of the weight on the cable. Your outstretched arm should be aligned with the cable. With your feet positioned shoulder width apart, squat down and grab the handle with both hands. Your arms should still be fully extended. In one motion, pull the handle up and across your body until your arms are in a fully-extended position above your head. Keep your back straight and your arms close to your body as you pivot your back foot and straighten your legs to get a full range of motion. Retract your arms and then your body. Return to the neutral position in a slow and controlled manner. Repeat to failure. Then, reposition and repeat the same series of movements on the opposite side.  Tip: You will twist your entire body with this exercise, but focus on getting maximal torso rotation and a strong clinch at the end of the movement. To ensure a good mind-muscle connection, keep your abs tense at all times."
        },
        {
            "name": "Dumbbell spell caster",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "dumbbell",
            "difficulty": "beginner",
            "workout_id": 2,
            "instructions": "Hold a dumbbell in each hand with a pronated grip. Your feet should be wide with your hips and knees extended. This will be your starting position. Begin the movement by pulling both of the dumbbells to one side next to your hip, rotating your torso. Keeping your arms straight and the dumbbells parallel to the ground, rotate your torso to swing the weights to your opposite side. Continue alternating, rotating from one side to the other until the set is complete."
        },
        {
            "name": "Decline reverse crunch",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "other",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Lie on your back on a decline bench and hold on to the top of the bench with both hands. Don't let your body slip down from this position. Hold your legs parallel to the floor using your abs to hold them there while keeping your knees and feet together. Tip: Your legs should be fully extended with a slight bend on the knee. This will be your starting position. While exhaling, move your legs towards the torso as you roll your pelvis backwards and you raise your hips off the bench. At the end of this movement your knees will be touching your chest. Hold the contraction for a second and move your legs back to the starting position while inhaling. Repeat for the recommended amount of repetitions.  Variations: You can do the movement on a flat surface and as you get more advanced you can use ankle weights."
        },
        {
            "name": "Spider crawl",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Begin in a prone position on the floor. Support your weight on your hands and toes, with your feet together and your body straight. Your arms should be bent to 90 degrees. This will be your starting position. Initiate the movement by raising one foot off of the ground. Externally rotate the leg and bring the knee toward your elbow, as far forward as possible. Return this leg to the starting position and repeat on the opposite side."
        },
        {
            "name": "Cocoons",
            "type": "strength",
            "muscle": "abdominals",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Begin by lying on your back on the ground. Your legs should be straight and your arms extended behind your head. This will be your starting position. To perform the movement, tuck the knees toward your chest, rotating your pelvis to lift your glutes from the floor. As you do so, flex the spine, bringing your arms back over your head to perform a simultaneous crunch motion. After a brief pause, return to the starting position."
        },
        {
            "name": "Hip Circles (Prone)",
            "type": "stretching",
            "muscle": "abductors",
            "equipment": "None",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Position yourself on your hands and knees on the ground. Maintaining good posture, raise one bent knee off of the ground. This will be your starting position. Keeping the knee in a bent position, rotate the femur in an arc, attempting to make a big circle with your knee. Perform this slowly for a number of repetitions, and repeat on the other side."
        },
        {
            "name": "Standing Hip Circles",
            "type": "stretching",
            "muscle": "abductors",
            "equipment": "body_only",
            "difficulty": "beginner",
            "workout_id": 3,
            "instructions": "Begin standing on one leg, holding to a vertical support. Raise the unsupported knee to 90 degrees. This will be your starting position. Open the hip as far as possible, attempting to make a big circle with your knee. Perform this movement slowly for a number of repetitions, and repeat on the other side."
        },
        {
            "name": "Clam",
            "type": "strength",
            "muscle": "abductors",
            "equipment": "None",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Begin by lying on your side on the ground. Support your head on your left arm. Flex the hips to 45 degrees and the knees to approximately 90 degrees, with your right leg directly on top of your left. This will be your starting position. Initiate the exercise by abducting your right leg, pushing your knee away from the midline of your body. Maintain contact between your feet throughout the movement. Pause at the top of the motion, and then return to the starting position. Repeat for the desired number of repetitions. Do both sides."
        },
        {
            "name": "Iliotibial band SMR",
            "type": "stretching",
            "muscle": "abductors",
            "equipment": "foam_roll",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Lay on your side, with the bottom leg placed onto a foam roller between the hip and the knee. The other leg can be crossed in front of you. Place as much of your weight as is tolerable onto your bottom leg; there is no need to keep your bottom leg in contact with the ground. Be sure to relax the muscles of the leg you are stretching. Roll your leg over the foam from you hip to your knee, pausing for 10-30 seconds at points of tension. Repeat with the opposite leg."
        },
        {
            "name": "Thigh abductor",
            "type": "strength",
            "muscle": "abductors",
            "equipment": "machine",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "To begin, sit down on the abductor machine and select a weight you are comfortable with. When your legs are positioned properly, grip the handles on each side. Your entire upper body (from the waist up) should be stationary. This is the starting position. Slowly press against the machine with your legs to move them away from each other while exhaling. Feel the contraction for a second and begin to move your legs back to the starting position while breathing in. Note: Remember to keep your upper body stationary to prevent any injuries from occurring. Repeat for the recommended amount of repetitions."
        },
        {
            "name": "Fire Hydrant",
            "type": "strength",
            "muscle": "abductors",
            "equipment": "body_only",
            "difficulty": "beginner",
            "workout_id": 3,
            "instructions": "Position yourself on your hands and knees on the ground. This will be your starting position. Keeping the knee in a bent position, abduct the femur, moving your knee away from the midline of the body. Pause at the top of the motion, and then slowly return to the starting position. Perform this slowly for a number of repetitions, and repeat on the other side."
        },
        {
            "name": "Windmills",
            "type": "stretching",
            "muscle": "abductors",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Lie on your back with your arms extended out to the sides and your legs straight. This will be your starting position. Lift one leg and quickly cross it over your body, attempting to touch the ground near the opposite hand. Return to the starting position, and repeat with the opposite leg. Continue to alternate for 10-20 repetitions."
        },
        {
            "name": "Monster Walk",
            "type": "strength",
            "muscle": "abductors",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Place a band around both ankles and another around both knees. There should be enough tension that they are tight when your feet are shoulder width apart. To begin, take short steps forward alternating your left and right foot. After several steps, do just the opposite and walk backward to where you started."
        },
        {
            "name": "IT Band and Glute Stretch",
            "type": "stretching",
            "muscle": "abductors",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Loop a belt, rope, or band around one of your feet, and swing that leg across your body to the opposite side, keeping the leg extended as you lay on the ground. This will be your starting position. Keeping your foot off of the floor, pull on the belt, using the tension to pull the toes up. Hold for 10-20 seconds, and repeat on the other side."
        },
        {
            "name": "Single-leg lying cross-over stretch",
            "type": "stretching",
            "muscle": "abductors",
            "equipment": "body_only",
            "difficulty": "beginner",
            "workout_id": 3,
            "instructions": "Lie on your back with your legs extended. Cross one leg over your body with the knee bent, attempting to touch the knee to the ground. Your partner should kneel beside you, holding your shoulder down with one hand and controlling the crossed leg with the other. this will be your starting position. Attempt to raise the bent knee off of the ground as your partner prevents any actual movement. After 10-20 seconds, relax the leg as your partner gently presses the knee towards the floor. Repeat with the other side."
        },
        {
            "name": "Dumbbell Bench Press",
            "type": "strength",
            "muscle": "chest",
            "equipment": "dumbbell",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Lie down on a flat bench with a dumbbell in each hand resting on top of your thighs. The palms of your hands will be facing each other. Then, using your thighs to help raise the dumbbells up, lift the dumbbells one at a time so that you can hold them in front of you at shoulder width. Once at shoulder width, rotate your wrists forward so that the palms of your hands are facing away from you. The dumbbells should be just to the sides of your chest, with your upper arm and forearm creating a 90 degree angle. Be sure to maintain full control of the dumbbells at all times. This will be your starting position. Then, as you breathe out, use your chest to push the dumbbells up. Lock your arms at the top of the lift and squeeze your chest, hold for a second and then begin coming down slowly. Tip: Ideally, lowering the weight should take about twice as long as raising it. Repeat the movement for the prescribed amount of repetitions of your training program.  Caution: When you are done, do not drop the dumbbells next to you as this is dangerous to your rotator cuff in your shoulders and others working out around you. Just lift your legs from the floor bending at the knees, twist your wrists so that the palms of your hands are facing each other and place the dumbbells on top of your thighs. When both dumbbells are touching your thighs simultaneously push your upper torso up (while pressing the dumbbells on your thighs) and also perform a slight kick forward with your legs (keeping the dumbbells on top of the thighs). By doing this combined movement, momentum will help you get back to a sitting position with both dumbbells still on top of your thighs. At this moment you can place the dumbbells on the floor. Variations: Another variation of this exercise is to perform it with the palms of the hands facing each other. Also, you can perform the exercise with the palms facing each other and then twisting the wrist as you lift the dumbbells so that at the top of the movement the palms are facing away from the body. I personally do not use this variation very often as it seems to be hard on my shoulders."
        },
        {
            "name": "Pushups",
            "type": "strength",
            "muscle": "chest",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Lie on the floor face down and place your hands about 36 inches apart while holding your torso up at arms length. Next, lower yourself downward until your chest almost touches the floor as you inhale. Now breathe out and press your upper body back up to the starting position while squeezing your chest. After a brief pause at the top contracted position, you can begin to lower yourself downward again for as many repetitions as needed.  Variations: If you are new at this exercise and do not have the strength to perform it, you can either bend your legs at the knees to take off resistance or perform the exercise against the wall instead of the floor. For the most advanced lifters, you can place your feet at a high surface such as a bench in order to increase the resistance and to target the upper chest more."
        },
        {
            "name": "Close-grip bench press",
            "type": "strength",
            "muscle": "chest",
            "equipment": "barbell",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Lie back on a flat bench. Using a close grip (around shoulder width), lift the bar from the rack and hold it straight over you with your arms locked. This will be your starting position. As you breathe in, come down slowly until you feel the bar on your middle chest. Tip: Make sure that - as opposed to a regular bench press - you keep the elbows close to the torso at all times in order to maximize triceps involvement. After a second pause, bring the bar back to the starting position as you breathe out and push the bar using your triceps muscles. Lock your arms in the contracted position, hold for a second and then start coming down slowly again. Tip: It should take at least twice as long to go down than to come up. Repeat the movement for the prescribed amount of repetitions. When you are done, place the bar back in the rack.  Caution: If you are new at this exercise, it is advised that you use a spotter. If no spotter is available, then be conservative with the amount of weight used. Also, beware of letting the bar drift too far forward. You want the bar to fall on your middle chest and nowhere else. Variations: This exercise can also be performed with an e-z bar using the inner handle as well as dumbbells, in which case the palms of the hands will be facing each other."
        },
        {
            "name": "Dumbbell Flyes",
            "type": "strength",
            "muscle": "chest",
            "equipment": "dumbbell",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Lie down on a flat bench with a dumbbell on each hand resting on top of your thighs. The palms of your hand will be facing each other. Then using your thighs to help raise the dumbbells, lift the dumbbells one at a time so you can hold them in front of you at shoulder width with the palms of your hands facing each other. Raise the dumbbells up like you're pressing them, but stop and hold just before you lock out. This will be your starting position. With a slight bend on your elbows in order to prevent stress at the biceps tendon, lower your arms out at both sides in a wide arc until you feel a stretch on your chest. Breathe in as you perform this portion of the movement. Tip: Keep in mind that throughout the movement, the arms should remain stationary; the movement should only occur at the shoulder joint. Return your arms back to the starting position as you squeeze your chest muscles and breathe out. Tip: Make sure to use the same arc of motion used to lower the weights. Hold for a second at the contracted position and repeat the movement for the prescribed amount of repetitions.  Variations: You may want to use a palms facing forward version for different stimulation."
        },
        {
            "name": "Incline dumbbell bench press",
            "type": "strength",
            "muscle": "chest",
            "equipment": "dumbbell",
            "difficulty": "intermediate",
            "workout_id": 3,
            "instructions": "Lie back on an incline bench with a dumbbell in each hand atop your thighs. The palms of your hands will be facing each other. Then, using your thighs to help push the dumbbells up, lift the dumbbells one at a time so that you can hold them at shoulder width. Once you have the dumbbells raised to shoulder width, rotate your wrists forward so that the palms of your hands are facing away from you. This will be your starting position. Be sure to keep full control of the dumbbells at all times. Then breathe out and push the dumbbells up with your chest. Lock your arms at the top, hold for a second, and then start slowly lowering the weight. Tip Ideally, lowering the weights should take about twice as long as raising them. Repeat the movement for the prescribed amount of repetitions. When you are done, place the dumbbells back on your thighs and then on the floor. This is the safest manner to release the dumbbells.  Variations: You can use several angles on the incline bench if the bench you are using is adjustable. Another variation of this exercise is to perform it with the palms of the hands facing each other. Also, you can perform the exercise with the palms facing each other and then twisting the wrist as you lift the dumbbells so that at the top of the movement the palms are facing away from the body. I personally do not use this variation very often as it seems to be hard on my shoulders."
        },
        {
            "name": "Low-cable cross-over",
            "type": "strength",
            "muscle": "chest",
            "equipment": "cable",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "To move into the starting position, place the pulleys at the low position, select the resistance to be used and grasp a handle in each hand. Step forward, gaining tension in the pulleys. Your palms should be facing forward, hands below the waist, and your arms straight. This will be your starting position. With a slight bend in your arms, draw your hands upward and toward the midline of your body. Your hands should come together in front of your chest, palms facing up. Return your arms back to the starting position after a brief pause."
        },
        {
            "name": "Barbell Bench Press - Medium Grip",
            "type": "strength",
            "muscle": "chest",
            "equipment": "barbell",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Lie back on a flat bench. Using a medium width grip (a grip that creates a 90-degree angle in the middle of the movement between the forearms and the upper arms), lift the bar from the rack and hold it straight over you with your arms locked. This will be your starting position. From the starting position, breathe in and begin coming down slowly until the bar touches your middle chest. After a brief pause, push the bar back to the starting position as you breathe out. Focus on pushing the bar using your chest muscles. Lock your arms and squeeze your chest in the contracted position at the top of the motion, hold for a second and then start coming down slowly again. Tip: Ideally, lowering the weight should take about twice as long as raising it. Repeat the movement for the prescribed amount of repetitions. When you are done, place the bar back in the rack.  Caution: If you are new at this exercise, it is advised that you use a spotter. If no spotter is available, then be conservative with the amount of weight used. Also, beware of letting the bar drift too far forward. You want the bar to touch your middle chest and nowhere else. Don't bounce the weight off your chest. You should be in full control of the barbell at all times."
        },
        {
            "name": "Chest dip",
            "type": "strength",
            "muscle": "chest",
            "equipment": "other",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "For this exercise you will need access to parallel bars. To get yourself into the starting position, hold your body at arms length (arms locked) above the bars. While breathing in, lower yourself slowly with your torso leaning forward around 30 degrees or so and your elbows flared out slightly until you feel a slight stretch in the chest. Once you feel the stretch, use your chest to bring your body back to the starting position as you breathe out. Tip: Remember to squeeze the chest at the top of the movement for a second. Repeat the movement for the prescribed amount of repetitions.  Variations: If you are new at this exercise and do not have the strength to perform it, use a dip assist machine if available. These machines use weight to help you push your bodyweight. Otherwise, a spotter holding your legs can help. More advanced lifters can add weight to the exercise by using a weight belt that allows the addition of weighted plates."
        },
        {
            "name": "Decline Dumbbell Flyes",
            "type": "strength",
            "muscle": "chest",
            "equipment": "dumbbell",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Secure your legs at the end of the decline bench and lie down with a dumbbell on each hand on top of your thighs. The palms of your hand will be facing each other. Once you are laying down, move the dumbbells in front of you at shoulder width. The palms of the hands should be facing each other and the arms should be perpendicular to the floor and fully extended. This will be your starting position. With a slight bend on your elbows in order to prevent stress at the biceps tendon, lower your arms out at both sides in a wide arc until you feel a stretch on your chest. Breathe in as you perform this portion of the movement. Tip: Keep in mind that throughout the movement, the arms should remain stationary; the movement should only occur at the shoulder joint. Return your arms back to the starting position as you squeeze your chest muscles and breathe out. Tip: Make sure to use the same arc of motion used to lower the weights. Hold for a second at the contracted position and repeat the movement for the prescribed amount of repetitions.  Variation: You may want to use a palms facing forward version for different stimulation."
        },
        {
            "name": "Bodyweight Flyes",
            "type": "strength",
            "muscle": "chest",
            "equipment": "e-z_curl_bar",
            "difficulty": "beginner",
            "workout_id": 1,
            "instructions": "Position two equally loaded EZ bars on the ground next to each other. Ensure they are able to roll. Assume a push-up position over the bars, supporting your weight on your toes and hands with your arms extended and body straight. Place your hands on the bars. This will be your starting position. Using a slow and controlled motion, move your hands away from the midline of your body, rolling the bars apart. Inhale during this portion of the motion. After moving the bars as far apart as you can, return to the starting position by pulling them back together. Exhale as you perform this movement."
        },
        {
            "name": "Barbell glute bridge",
            "type": "powerlifting",
            "muscle": "glutes",
            "equipment": "barbell",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Begin seated on the ground with a loaded barbell over your legs. Using a fat bar or having a pad on the bar can greatly reduce the discomfort caused by this exercise. Roll the bar so that it is directly above your hips, and lay down flat on the floor. Begin the movement by driving through with your heels, extending your hips vertically through the bar. Your weight should be supported by your upper back and the heels of your feet. Extend as far as possible, then reverse the motion to return to the starting position."
        },
        {
            "name": "Barbell Hip Thrust",
            "type": "powerlifting",
            "muscle": "glutes",
            "equipment": "barbell",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Begin seated on the ground with a bench directly behind you. Have a loaded barbell over your legs. Using a fat bar or having a pad on the bar can greatly reduce the discomfort caused by this exercise. Roll the bar so that it is directly above your hips, and lean back against the bench so that your shoulder blades are near the top of it. Begin the movement by driving through your feet, extending your hips vertically through the bar. Your weight should be supported by your shoulder blades and your feet. Extend as far as possible, then reverse the motion to return to the starting position."
        },
        {
            "name": "Single-leg cable hip extension",
            "type": "strength",
            "muscle": "glutes",
            "equipment": "cable",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Hook a leather ankle cuff to a low cable pulley and then attach the cuff to your ankle. Face the weight stack from a distance of about two feet, grasping the steel frame for support. While keeping your knees and hips bent slightly and your abs tight, contract your glutes to slowly \"kick\" the working leg back in a semicircular arc as high as it will comfortably go as you breathe out. Tip: At full extension, squeeze your glutes for a second in order to achieve a peak contraction. Now slowly bring your working leg forward, resisting the pull of the cable until you reach the starting position. Repeat for the recommended amount of repetitions. Switch legs and repeat the movement for the other side.  Variations: You can perform this exercise with exercise bands."
        },
        {
            "name": "Glute bridge",
            "type": "strength",
            "muscle": "glutes",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Lie flat on the floor on your back with the hands by your side and your knees bent. Your feet should be placed around shoulder width. This will be your starting position. Pushing mainly with your heels, lift your hips off the floor while keeping your back straight. Breathe out as you perform this part of the motion and hold at the top for a second. Slowly go back to the starting position as you breathe in.  Variations: You can perform this exercise one leg at a time."
        },
        {
            "name": "Single-leg glute bridge",
            "type": "strength",
            "muscle": "glutes",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 1,
            "instructions": "Lay on the floor with your feet flat and knees bent. Raise one leg off of the ground, pulling the knee to your chest. This will be your starting position. Execute the movement by driving through the heel, extending your hip upward and raising your glutes off of the ground. Extend as far as possible, pause and then return to the starting position."
        },
        {
            "name": "Step-up with knee raise",
            "type": "strength",
            "muscle": "glutes",
            "equipment": "body_only",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Stand facing a box or bench of an appropriate height with your feet together. This will be your starting position. Begin the movement by stepping up, putting your left foot on the top of the bench. Extend through the hip and knee of your front leg to stand up on the box. As you stand on the box with your left leg, flex your right knee and hip, bringing your knee as high as you can. Reverse this motion to step down off the box, and then repeat the sequence on the opposite leg."
        },
        {
            "name": "Kettlebell thruster",
            "type": "strength",
            "muscle": "glutes",
            "equipment": "kettlebells",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "Clean two kettlebells to your shoulders. Clean the kettlebells to your shoulders by extending through the legs and hips as you pull the kettlebells towards your shoulders. Rotate your wrists as you do so. This will be your starting position. Begin to squat by flexing your hips and knees, lowering your hips between your legs. Maintain an upright, straight back as you descend as low as you can. At the bottom, reverse direction and squat by extending your knees and hips, driving through your heels. As you do so, press both kettlebells overhead by extending your arms straight up, using the momentum from the squat to help drive the weights upward. As you begin the next repetition, return the weights to the shoulders."
        },
        {
            "name": "Kneeling Squat",
            "type": "powerlifting",
            "muscle": "glutes",
            "equipment": "barbell",
            "difficulty": "beginner",
            "workout_id": 2,
            "instructions": "Set the bar to the proper height in a power rack. Kneel behind the bar; it may be beneficial to put a mat down to pad your knees. Slide under the bar, racking it across the back of your shoulders. Your shoulder blades should be retracted and the bar tight across your back. Unrack the weight. With your head looking forward, sit back with your butt until you touch your calves. Reverse the motion, returning the torso to an upright position."
        },
        {
            "name": "Flutter Kicks",
            "type": "strength",
            "muscle": "glutes",
            "equipment": "None",
            "difficulty": "intermediate",
            "workout_id": 2,
            "instructions": "On a flat bench lie facedown with the hips on the edge of the bench, the legs straight with toes high off the floor and with the arms on top of the bench holding on to the front edge. Squeeze your glutes and hamstrings and straighten the legs until they are level with the hips. This will be your starting position. Start the movement by lifting the left leg higher than the right leg. Then lower the left leg as you lift the right leg. Continue alternating in this manner (as though you are doing a flutter kick in water) until you have done the recommended amount of repetitions for each leg. Make sure that you keep a controlled movement at all times. Tip: You will breathe normally as you perform this movement.  Variations: As you get more advanced you can use ankle weights."
        },
        {
            "name": "Glute Kickback",
            "type": "strength",
            "muscle": "glutes",
            "equipment": "body_only",
            "difficulty": "beginner",
            "workout_id": 2,
            "instructions": "Kneel on the floor or an exercise mat and bend at the waist with your arms extended in front of you (perpendicular to the torso) in order to get into a kneeling push-up position but with the arms spaced at shoulder width. Your head should be looking forward and the bend of the knees should create a 90-degree angle between the hamstrings and the calves. This will be your starting position. As you exhale, lift up your right leg until the hamstrings are in line with the back while maintaining the 90-degree angle bend. Contract the glutes throughout this movement and hold the contraction at the top for a second. Tip: At the end of the movement the upper leg should be parallel to the floor while the calf should be perpendicular to it. Go back to the initial position as you inhale and now repeat with the left leg. Continue to alternate legs until all of the recommended repetitions have been performed.  Variations: For this exercise you can also perform all of the repetitions with one leg first and then the other one. Additionally, you can also add ankle weights."
        }
        ]  

    for exercise in exercises:

        new_exercise = Exercise(
            name = exercise["name"],
            muscle = exercise["muscle"],
            type = exercise["type"],
            equipment = exercise["equipment"],
            difficulty = exercise["difficulty"],
            instructions = exercise["instructions"],
            image_url = exercise["image_url"],
            sub_muscle = exercise["sub_muscle"],
            workout_id = exercise["workout_id"]
        )

        db.session.add(new_exercise)
        
    db.session.commit()
    print('Exercises were succesfully created')


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_exercise():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
