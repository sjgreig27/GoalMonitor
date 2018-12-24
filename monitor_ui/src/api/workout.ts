import {Lift, WorkoutPlan, Workout, PlannedLift, LiftRecord, Set} from "../types/workout";
import {get, post, request, API_ROOT} from '../utils/ApiUtils';

const WORKOUT_API_ROOT = API_ROOT + 'workout/';

export function getLifts(): Promise<Lift[]>{
    return get<Lift[]>(WORKOUT_API_ROOT + 'lift')
}

export function getWorkoutPlans(): Promise<WorkoutPlan[]>{
    return get<WorkoutPlan[]>(WORKOUT_API_ROOT + 'workout-plan')
}

export function getWorkouts(): Promise<Workout[]>{
    return get<Workout[]>(WORKOUT_API_ROOT + 'workout')
}

export function getPlannedLifts(): Promise<PlannedLift[]>{
    return get<PlannedLift[]>(WORKOUT_API_ROOT + 'planned-lift')
}

export function getLiftRecords(): Promise<LiftRecord[]>{
    return get<LiftRecord[]>(WORKOUT_API_ROOT + 'lift-record')
}

export function getSets(): Promise<Set[]>{
    return get<Set[]>(WORKOUT_API_ROOT + 'set')
}