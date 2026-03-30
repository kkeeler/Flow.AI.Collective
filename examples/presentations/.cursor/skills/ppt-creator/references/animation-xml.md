# Animation XML for Click-to-Advance

Inject this XML into a slide's `<p:timing>` element to make layered images appear one-per-click. Each `<p:par>` block represents one click. Replace `SPID_N` with the `shape_id` of each layered image.

## How It Works

- All layered images start invisible (placed on the slide but behind the base frame).
- On each click, one image fades in over the previous, creating the illusion of animation.
- The `delay="indefinite"` on each `<p:par>` means "wait for a mouse click."
- `spid` is the shape's internal ID — get it from `shape.shape_id` after adding with `add_picture()`.

## Template

For a slide with N animation steps (N+1 total images: 1 base + N overlays):

```xml
<p:timing xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main">
  <p:tnLst>
    <p:par>
      <p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">
        <p:childTnLst>
          <p:seq concurrent="1" nextAc="seek">
            <p:cTn id="2" dur="indefinite" nodeType="mainSeq">
              <p:childTnLst>

                <!-- Click 1: reveal step-1 image -->
                <p:par>
                  <p:cTn id="3" fill="hold">
                    <p:stCondLst>
                      <p:cond delay="indefinite"/>
                    </p:stCondLst>
                    <p:childTnLst>
                      <p:par>
                        <p:cTn id="4" fill="hold">
                          <p:stCondLst><p:cond delay="0"/></p:stCondLst>
                          <p:childTnLst>
                            <p:par>
                              <p:cTn id="5" presetID="10" presetClass="entr"
                                     presetSubtype="0" fill="hold" nodeType="clickEffect">
                                <p:stCondLst><p:cond delay="0"/></p:stCondLst>
                                <p:childTnLst>
                                  <p:set>
                                    <p:cBhvr>
                                      <p:cTn id="6" dur="1" fill="hold">
                                        <p:stCondLst><p:cond delay="0"/></p:stCondLst>
                                      </p:cTn>
                                      <p:tgtEl>
                                        <p:spTgt spid="SPID_1"/>
                                      </p:tgtEl>
                                      <p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>
                                    </p:cBhvr>
                                    <p:to><p:strVal val="visible"/></p:to>
                                  </p:set>
                                  <p:animEffect transition="in" filter="fade">
                                    <p:cBhvr>
                                      <p:cTn id="7" dur="500"/>
                                      <p:tgtEl>
                                        <p:spTgt spid="SPID_1"/>
                                      </p:tgtEl>
                                    </p:cBhvr>
                                  </p:animEffect>
                                </p:childTnLst>
                              </p:cTn>
                            </p:par>
                          </p:childTnLst>
                        </p:cTn>
                      </p:par>
                    </p:childTnLst>
                  </p:cTn>
                </p:par>

                <!-- Click 2: reveal step-2 image (duplicate the block, increment IDs, use SPID_2) -->
                <!-- ... repeat for each additional step ... -->

              </p:childTnLst>
            </p:cTn>
            <p:prevCondLst>
              <p:cond evt="onPrev" delay="0">
                <p:tgtEl><p:sldTgt/></p:tgtEl>
              </p:cond>
            </p:prevCondLst>
            <p:nextCondLst>
              <p:cond evt="onNext" delay="0">
                <p:tgtEl><p:sldTgt/></p:tgtEl>
              </p:cond>
            </p:nextCondLst>
          </p:seq>
        </p:childTnLst>
      </p:cTn>
    </p:par>
  </p:tnLst>
</p:timing>
```

## Generating XML Programmatically

Rather than manually duplicating XML blocks, build them in a loop. For each click step:

1. Create the `<p:par>` wrapper with `delay="indefinite"`.
2. Inside, add `<p:set>` to make the shape visible and `<p:animEffect>` for the fade.
3. Increment `cTn` id values sequentially (must be unique per slide).
4. Reference the correct `spid` for that step's image.

Use `lxml.etree.fromstring()` to parse the XML template, then inject into `slide._element`.
