import * as moment from 'moment';
import {User} from "./users";

export type WeekDay = 'Monday' | 'Tuesday' | 'Wednesday' | 'Thursday' | 'Friday' | 'Saturday' | 'Sunday'

export interface Lift {
    name: string
}

export interface WorkoutPlan {
    name: string
}

export interface Workout {
    day: WeekDay,
    plan: WorkoutPlan
}

export interface PlannedLift {
    lift: Lift,
    workout: Workout
}

export interface LiftRecord {
    plannedLift: PlannedLift,
    timestamp: moment.Moment,
    user: User
}

export interface Set {
    lift: LiftRecord,
    numberOfReps: number,
    weightInKg: number
}