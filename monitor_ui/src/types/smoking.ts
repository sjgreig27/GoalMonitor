import * as moment from 'moment';


interface NicotineProduct {
    timestamp: moment.Moment,
    comment: string,
    costInPounds: number,
}

export interface Cigarette extends NicotineProduct {
    strengthInMg: number
}

export type CigarettePacket = Cigarette;

export interface Vapour extends NicotineProduct {
    strengthInMgMl: number,
    volume: number
}