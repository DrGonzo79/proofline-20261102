import fixtures from "../data/demo_candidates.json";
export type Candidate=(typeof fixtures)[number];
export const candidates=fixtures as Candidate[];
export type Decision={score:number;band:"verified"|"review"|"insufficient";reasons:string[];credentialId:string};
export function assess(c:Candidate,consent:boolean):Decision{
 if(!consent) throw new Error("Confirm candidate consent before generating a proof pack.");
 const continuity=Math.min(30,c.repo.active_weeks/4),contribution=Math.min(25,(c.repo.merged_prs+c.repo.reviewed_prs*.35)/5),tenure=Math.min(15,c.repo.months*.6),oral=((c.defense.architecture+c.defense.tradeoffs+c.defense.ownership)/15)*30;
 const score=Math.round(continuity+contribution+tenure+oral);
 return {score,band:score>=78?"verified":score>=60?"review":"insufficient",reasons:[`${c.repo.active_weeks} active weeks verified locally`,`${c.repo.merged_prs} merged and ${c.repo.reviewed_prs} reviewed PRs summarized`,`${Math.round(oral)}/30 oral-defense points`],credentialId:`PF-${c.id.toUpperCase()}-${score}`};
}
