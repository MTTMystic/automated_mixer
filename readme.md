A script to use in conjunction with Audacity that automatically imports and mixes given audio files in m4a or mp3 format. An update to the first rudimentary quick proof-of-concept:

https://github.com/MTTMystic/automated_mixer_old

Which I had never expected to use so much that I would make it more of a personal passion project and utility for my own creative endeavors in audio mixing as a personal hobby. I now designed and fully intend to leverage my skills in a revamped full-featured program more sophisticated (and structured) than the original.

#12-29-2024
Decided to go in a completely different design direction while building a batch handler to automatically process a huge list of audio files (from given folder) then segment into batches of configurable size with configurable valid file formats as validation is included with batch generation and user prompts / error reporting done in separate module.

The (as of now) overdone error reporting and even possibly overdone config considerations are (in terms of the automated error reporter) a separate project entirely worth considering for dev or doc usage, and also (in terms of dev and user config loading for the auto-mixer) not a first priority for literal use as a interactive script for minimal loss of import or other mixing progress as intention is for user to control separate batch mixing and now be able to stop and save or specifically configure each batch fine-tuning each part, mixing and saving to separate files if specifically desired, and minimize making it a pain to process large numbers of files at once. 