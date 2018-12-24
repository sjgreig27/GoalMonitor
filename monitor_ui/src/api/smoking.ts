import {Cigarette, CigarettePacket, Vapour} from "../types/smoking";
import {get, post, request, API_ROOT} from '../utils/ApiUtils';

const SMOKING_API_ROOT = API_ROOT + 'smoking/';

export function getCigarrettes(): Promise<Cigarette[]>{
    return get<Cigarette[]>(SMOKING_API_ROOT + 'cigarette')
}

export function getCigarrettePackets(): Promise<CigarettePacket[]>{
    return get<CigarettePacket[]>(SMOKING_API_ROOT + 'cigarette-packet')
}

export function getVapours(): Promise<Vapour[]>{
    return get<Vapour[]>(SMOKING_API_ROOT + 'vapour')
}